#!/usr/bin/env python3
"""
YouTube Transcript Fetcher, Summarizer & Q&A Tool

Usage:
    python3 youtube_transcript_qa.py <youtube_url_or_id> [--language en,tr] [--out_dir DIR] [--summarize] [--question "What is..."]

Description:
    1. Fetches the transcript from a YouTube video.
    2. Saves the raw transcript to a text file (transcript.txt).
    3. Optionally generates a summary using the configured LLM provider (transcript_summary.md).
    4. Optionally answers a user question grounded in the transcript (transcript_qa.txt).

The LLM queries use the openai-compatible endpoint. If OPENAI_API_KEY is set,
it is used directly; otherwise the script reads ~/.hermes/config.yaml for
provider settings (e.g. openrouter base_url + api_key).

Dependencies:
    pip install youtube-transcript-api pyyaml openai
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# YouTube transcript fetching
# ---------------------------------------------------------------------------

def extract_video_id(url_or_id: str) -> str:
    """Extract the 11-character video ID from various YouTube URL formats."""
    url_or_id = url_or_id.strip()
    patterns = [
        r'(?:v=|youtu\.be/|shorts/|embed/|live/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$',
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id


def format_timestamp(seconds: float) -> str:
    """Convert seconds to MM:SS or HH:MM:SS format."""
    total = int(seconds)
    h, remainder = divmod(total, 3600)
    m, s = divmod(remainder, 60)
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def fetch_transcript(video_id: str, languages=None):
    """Fetch transcript segments from YouTube.

    Returns a list of dicts with 'text', 'start', and 'duration' keys.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("Error: youtube-transcript-api not installed. Run: pip install youtube-transcript-api",
              file=sys.stderr)
        sys.exit(1)

    api = YouTubeTranscriptApi()
    if languages:
        result = api.fetch(video_id, languages=languages)
    else:
        result = api.fetch(video_id)

    # v1.x returns FetchedTranscriptSnippet objects; normalize to dicts
    return [
        {"text": seg.text, "start": seg.start, "duration": seg.duration}
        for seg in result
    ]


# ---------------------------------------------------------------------------
# LLM helpers (for summarization and Q&A)
# ---------------------------------------------------------------------------

def load_llm_config():
    """Load LLM config from ~/.hermes/config.yaml as fallback.

    Returns (api_key, base_url, model) or (None, None, None).
    """
    config_path = Path.home() / ".hermes" / "config.yaml"
    if not config_path.exists():
        return None, None, None

    try:
        import yaml
        with open(config_path) as f:
            cfg = yaml.safe_load(f)

        # Prefer openrouter provider (this environment's default)
        providers = cfg.get("providers", {})
        openrouter = providers.get("openrouter", {})
        if openrouter.get("api_key") and openrouter.get("base_url"):
            model = cfg.get("model", {}).get("default", "poolside/laguna-s-2.1:free")
            return openrouter["api_key"], openrouter["base_url"], model

        # Fallback to openai provider
        openai_cfg = providers.get("openai", {})
        if openai_cfg.get("api_key"):
            model = openai_cfg.get("model", "gpt-3.5-turbo")
            return openai_cfg["api_key"], openai_cfg.get("base_url"), model

    except Exception:
        pass

    return None, None, None


def get_openai_client():
    """Create an OpenAI-compatible client, reading env first then config."""
    api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("TINKER_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL")
    model = os.environ.get("OPENAI_MODEL") or os.environ.get("MODEL")

    if not api_key or not base_url:
        # Fall back to Hermes config.yaml
        cfg_key, cfg_url, cfg_model = load_llm_config()
        if cfg_key and cfg_url:
            api_key = api_key or cfg_key
            base_url = base_url or cfg_url
            model = model or cfg_model

    if not api_key or not base_url:
        print("Error: No LLM credentials found. Set OPENAI_API_KEY and OPENAI_BASE_URL, "
              "or configure providers in ~/.hermes/config.yaml", file=sys.stderr)
        sys.exit(1)

    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai package not installed. Run: pip install openai", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(api_key=api_key, base_url=base_url)
    return client, model


def call_llm(client, model, system_prompt, user_prompt, max_tokens=4000):
    """Call the LLM and return the response text."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=max_tokens,
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling LLM: {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def chunk_text(text, max_chars=12000):
    """Split long text into chunks of ~max_chars characters, attempting
    sentence boundaries. Returns a list of strings."""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    current = ""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    for sent in sentences:
        if len(current) + len(sent) + 1 <= max_chars:
            current = current + " " + sent if current else sent
        else:
            if current:
                chunks.append(current)
            current = sent
    if current:
        chunks.append(current)
    return chunks


def main():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube transcript, save to file, summarize, and answer Q&A"
    )
    parser.add_argument("url", help="YouTube URL or video ID")
    parser.add_argument("--language", "-l", default=None,
                        help="Comma-separated language codes (e.g. en,tr). Default: auto")
    parser.add_argument("--out_dir", "-o", default="/root/media/youtube-content",
                        help="Output directory for transcript files (default: /root/media/youtube-content)")
    parser.add_argument("--summarize", "-s", action="store_true",
                        help="Generate a summary of the transcript")
    parser.add_argument("--question", "-q", default=None,
                        help="Ask a question about the transcript content")
    parser.add_argument("--timestamps", "-t", action="store_true",
                        help="Include timestamps in the saved transcript file")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    languages = [l.strip() for l in args.language.split(",")] if args.language else None

    # Fetch transcript
    try:
        segments = fetch_transcript(video_id, languages)
    except Exception as e:
        err = str(e)
        if "disabled" in err.lower():
            print("Error: Transcripts are disabled for this video.", file=sys.stderr)
        elif "no transcript" in err.lower() or "not found" in err.lower():
            print("Error: No transcript found. Try specifying a language with --language.", file=sys.stderr)
        else:
            print(f"Error fetching transcript: {err}", file=sys.stderr)
        sys.exit(1)

    full_text = " ".join(seg["text"] for seg in segments)
    timestamped = "\n".join(
        f"{format_timestamp(seg['start'])} {seg['text']}" for seg in segments
    )

    # Save transcript
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    transcript_file = out_dir / "transcript.txt"
    if args.timestamps:
        transcript_file.write_text(timestamped, encoding="utf-8")
    else:
        transcript_file.write_text(full_text, encoding="utf-8")
    print(f"Transcript saved to: {transcript_file}")

    # Metadata file with JSON info
    meta = {
        "video_id": video_id,
        "url": args.url,
        "language": languages[0] if languages else "auto",
        "segment_count": len(segments),
        "duration": format_timestamp(segments[-1]["start"] + segments[-1]["duration"]) if segments else "0:00",
        "transcript_file": str(transcript_file),
    }
    meta_file = out_dir / "metadata.json"
    meta_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Metadata saved to: {meta_file}")

    # Print summary to stdout
    print(f"\n--- Transcript Summary ---")
    print(f"Video ID: {video_id}")
    print(f"Segments: {len(segments)}")
    print(f"Duration: ~{meta['duration']}")
    print(f"Characters: {len(full_text)}")

    # Show first few lines as a preview
    print(f"\n--- Preview (first 5 segments) ---")
    for seg in segments[:5]:
        print(f"  {format_timestamp(seg['start'])} {seg['text'][:100]}")

    # Generate summary
    if args.summarize:
        client, model = get_openai_client()

        system_prompt = (
            "You are a skilled content summarizer. Read the transcript below and produce "
            "a clear, well-structured summary in markdown. Include:\n"
            "1. A concise title\n"
            "2. 5-8 key bullet-point takeaways covering the main arguments, claims, and conclusions\n"
            "3. If the transcript is very long, organize by topic sections with subheadings\n\n"
            "Focus on the most important and surprising insights. Keep the summary readable and "
            "avoid filler. Write in the third person."
        )

        user_prompt = f"Transcript:\n\n{full_text}"

        # Chunk if needed
        if len(full_text) > 12000:
            chunks = chunk_text(full_text, max_chars=12000)
            summaries = []
            for i, chunk in enumerate(chunks):
                print(f"Summarizing chunk {i+1}/{len(chunks)}...")
                chunk_prompt = f"Transcript Part {i+1}/{len(chunks)}:\n\n{chunk}"
                s = call_llm(client, model, system_prompt, chunk_prompt, max_tokens=3000)
                summaries.append(s)
            combined = "\n\n---\n\n".join(summaries)

            # Final consolidation
            consolidation_prompt = (
                f"The following are partial summaries of a YouTube video transcript. "
                f"Consolidate them into a single coherent summary with:\n"
                f"1. A concise title\n"
                f"2. 5-8 key bullet-point takeaways\n"
                f"3. Topic sections if applicable\n\n"
                f"Partial summaries:\n\n{combined}"
            )
            summary_text = call_llm(client, model, system_prompt, consolidation_prompt, max_tokens=3000)
        else:
            summary_text = call_llm(client, model, system_prompt, user_prompt, max_tokens=4000)

        summary_file = out_dir / "transcript_summary.md"
        summary_file.write_text(summary_text, encoding="utf-8")
        print(f"\nSummary saved to: {summary_file}")
        print(f"\n--- Summary ---")
        # Print as much as fits
        if len(summary_text) <= 3000:
            print(summary_text)
        else:
            print(summary_text[:3000])
            print(f"\n... (full summary in {summary_file})")

    # Answer question
    if args.question:
        client, model = get_openai_client()

        system_prompt = (
            "You are a helpful assistant that answers questions strictly based on the "
            "YouTube video transcript provided. If the answer cannot be found in the transcript, "
            "say so clearly rather than guessing or making things up. Be concise but thorough."
        )

        # If transcript is long, use just enough context
        if len(full_text) > 12000:
            chunks = chunk_text(full_text, max_chars=12000)
            # Find the most relevant chunk by keyword overlap
            keywords = set(args.question.lower().split())
            best_chunk = chunks[0]
            best_score = 0
            for chunk in chunks:
                chunk_words = set(chunk.lower().split())
                score = len(keywords & chunk_words)
                if score > best_score:
                    best_score = score
                    best_chunk = chunk
            context = best_chunk
        else:
            context = full_text

        user_prompt = f"Question: {args.question}\n\nTranscript:\n\n{context}"

        answer = call_llm(client, model, system_prompt, user_prompt, max_tokens=4000)

        qa_file = out_dir / "transcript_qa.txt"
        qa_file.write_text(f"Q: {args.question}\n\nA: {answer}\n", encoding="utf-8")
        print(f"\nQ&A saved to: {qa_file}")
        print(f"\n--- Answer ---")
        print(answer)


if __name__ == "__main__":
    main()