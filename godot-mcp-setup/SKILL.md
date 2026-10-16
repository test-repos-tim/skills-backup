---
name: godot-mcp-setup
description: Setup and run Godot MCP server to control Godot game engine from Hermes Agent.
version: 1.0.0
author: Hermes Agent
---

# Godot MCP Server Setup and Usage

## Description
This skill provides steps to set up and run the Godot Model Context Protocol (MCP) server, allowing control of the Godot game engine from Hermes Agent.

## Prerequisites
- Node.js >=18 installed
- Godot Engine binary available (tested with 4.3+)
- Access to the godot-mcp repository (located at `/home/shiva/godot/godot-mcp` in this environment)

## Setup Steps

1. **Navigate to the godot-mcp directory**
   ```bash
   cd /home/shiva/godot/godot-mcp
   ```

2. **Install Node.js dependencies** (if not already installed)
   ```bash
   npm install
   ```
   This will also run the `prepare` script which compiles TypeScript to JavaScript in the `build/` directory.

3. **(Optional) Build manually** if you prefer to build separately
   ```bash
   npm run build
   ```
   *Note: Use `npm run build` (not `npm build`)*.

4. **Set the Godot executable path**
   Replace `/path/to/godot` with the actual path to your Godot binary.
   ```bash
   export GODOT_PATH="/home/shiva/godot/Godot_v4.7.1-stable_linux.x86_64"
   ```
   Note: This export is valid for the current shell session. For reuse in other sessions, you may add it to your shell startup file as per your preference.

5. **Enable debug logging (optional)**
   ```bash
   export DEBUG="true"
   ```

6. **Start the MCP server**
   You can start the server directly via Node:
   ```bash
   node build/index.js
   ```
   Alternatively, if you have linked or installed the package locally, you can use the provided binary:
   ```bash
   ./build/index.js
   ```

## Troubleshooting

- **"Could not find Godot in common locations"**: Ensure `GODOT_PATH` is set correctly and points to an executable Godot binary.
- **Permission denied**: Make sure the Godot binary has execute permissions (`chmod +x /path/to/godot`).
- **Missing dependencies**: If `npm install` fails, try clearing the cache and reinstalling:
  ```bash
  npm cache clean --force
  npm install
  ```
- **Version mismatch**: The server expects Godot 4.3 or newer for full feature compatibility.

## Notes
- The server logs errors and diagnostics to stderr, which does not interfere with MCP JSON-RPC communication over stdout.
- To stop the server, press `Ctrl+C` in the terminal where it is running.
- **Important**: This Godot MCP server implementation does *not* support the standard MCP prompts or resources endpoints (attempts to list prompts/resources will return "Method not found"). Natural language interaction must be achieved through Hermes Agent's direct tool-calling capabilities using the available mcp_godot_mcp_* tools.
- For natural-language-like interaction, use Hermes Agent's reasoning to break down requests into specific tool calls (e.g., use `mcp_godot_mcp_get_project_info` to inspect a project, then `mcp_godot_mcp_create_scene` and `mcp_godot_mcp_add_node` to build scenes).

## Example Usage from Hermes Agent
Once the server is running, you can use Hermes Agent's MCP tooling to call tools like `get_project_info`, `create_scene`, `add_node`, etc., by connecting to the stdio interface.

### Available Tools for Natural-Language-Like Interaction
While this MCP server doesn't support predefined prompts/resources for natural language prompts, you can achieve similar functionality by using Hermes Agent's reasoning to combine these available tools:

- `mcp_godot_mcp_get_godot_version` - Check Godot version
- `mcp_godot_mcp_get_project_info` - Get project details (requires projectPath)
- `mcp_godot_mcp_list_projects` - List Godot projects in a directory
- `mcp_godot_mcp_create_scene` - Create new scenes
- `mcp_godot_mcp_add_node` - Add nodes to scenes
- `mcp_godot_mcp_load_sprite` - Load sprites into Sprite2D nodes
- `mcp_godot_mcp_run_project` - Run Godot projects
- `mcp_godot_mcp_save_scene` - Save scenes
- `mcp_godot_mcp_stop_project` - Stop running projects
- `mcp_godot_mcp_launch_editor` - Launch Godot editor
- `mcp_godot_mcp_get_debug_output` - Get debug output
- `mcp_godot_mcp_export_mesh_library` - Export mesh libraries
- `mcp_godot_mcp_get_uid` - Get resource UIDs (Godot 4.4+)
- `mcp_godot_mcp_update_project_uids` - Update UIDs (Godot 4.4+)

### Example Workflow for Scene Creation
To create a simple scene through natural-language-like requests:
1. First, get project info: `mcp_godot_mcp_get_project_info` with your project path
2. Create a scene: `mcp_godot_mcp_create_scene` with root node type and path
3. Add nodes: Use `mcp_godot_mcp_add_node` multiple times to build your scene hierarchy
4. Load resources: Use `mcp_godot_mcp_load_sprite` for sprite nodes
5. Save the scene: `mcp_godot_mcp_save_scene`