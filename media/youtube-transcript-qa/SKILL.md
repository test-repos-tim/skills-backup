---
name: youtube-transcript-qa
description: "Fetch YouTube transcripts to text files, generate summaries, and answer questions about content."
platforms: [linux, macos, windows]
---

# YouTube Transcript Fetcher, Summarizer & Q&A

## When to use

Use this skill when the user provides a YouTube URL or video ID and asks to:
- Save a transcript to a text file
- Generate a summary of the important details in a video
- Answer questions about information contained in a video transcript

## Setup

Install the required Python dependencies:

```bash
pip install youtube-transcript-api pyyaml openai
```

The script reads LLM credentials in this order of precedence:
1. Environment variables: `OPENAI_API_KEY` (or `TINKER_API_KEY`), `OPENAI_BASE_URL`, `OPENAI_MODEL`
2. Fallback: `~/.hermes/config.yaml` provider settings (e.g. openrouter)

## Helper Script

`SKILL_DIR` is the directory containing this SKILL.md file.

```bash
# Basic: fetch transcript and save to text file
python3 SKILL_DIR/scripts/youtube_transcript_qa.py "https://youtube.com/watch?v=VIDEO_ID"

# Fetch and generate a summary
python3 SKILL_DIR/scripts/youtube_transcript_qa.py "URL" --summarize

# Fetch, save, and answer a specific question
python3 SKILL_DIR/scripts/youtube_transcript_qa.py "URL" --summarize --question "What are the main takeaways?"

# Specify language preference
python3 SKILL_DIR/scripts/youtube_transcript_qa.py "URL" --language en

# Save transcript with timestamps
python3 SKILL_DIR/scripts/youtube_transcript_qa.py "URL" --timestamps

# Custom output directory
python3 SKILL_DIR/scripts/youtube_transcript_qa.py "URL" --summarize --out_dir /path/to/output
```

### Arguments

| Argument | Short | Description |
|---|---|---|
| `url` | | YouTube URL or raw 11-character video ID (positional, required) |
| `--summarize` | `-s` | Generate a markdown summary of key points |
| `--question` | `-q` | Answer a specific question about the transcript |
| `--language` | `-l` | Comma-separated language codes (e.g. `en,es`). Default: auto |
| `--timestamps` | `-t` | Include HH:MM:SS timestamps in the saved transcript file |
| `--out_dir` | `-o` | Output directory (default: `/root/media/youtube-content`) |

## Output Files

All files are written to the output directory (default: `/root/media/youtube-content/`):

| File | Description |
|---|---|
| `transcript.txt` | The full transcript as plain text |
| `metadata.json` | Video ID, URL, language, segment count, duration |
| `transcript_summary.md` | Markdown summary with title and key takeaways |
| `transcript_qa.txt` | Question and AI-generated answer |

## Workflow

1. **Fetch** the transcript using the helper script with the YouTube URL.
2. **Save** the raw transcript to `transcript.txt` (plain text or with timestamps).
3. **Summarize** (with `--summarize`): the LLM reads the transcript and produces a structured summary with a title, 5-8 key bullet points, and topic sections if the video is long. Long transcripts are automatically chunked and consolidated.
4. **Answer questions** (with `--question "What is..."`): the LLM is grounded in the transcript text and answers strictly from the content. If the answer is not in the transcript, the LLM says so rather than hallucinating.

## Error Handling

- **Transcripts disabled**: the video likely has no captions. Try `--language` to check for alternate language tracks.
- **Private/unavailable video**: verify the URL is correct and the video is public.
- **No matching language**: the script retries with auto-detection; check the video page for available subtitle languages.
- **LLM not configured**: set `OPENAI_API_KEY` and `OPENAI_BASE_URL` environment variables, or ensure `~/.hermes/config.yaml` has provider settings.
- **Long transcripts**: transcripts exceeding ~12,000 characters are automatically split into chunks for summarization, and relevant chunks are selected for Q&A.