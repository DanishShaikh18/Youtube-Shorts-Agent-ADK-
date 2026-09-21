# YouTube Shorts Agent (ADK Learning Project)

This project is a learning exercise to explore and demonstrate the capabilities of the **Google Agent Development Kit (ADK)**. It implements a multi-agent system designed to automatically generate concepts, scripts, and visual ideas for YouTube Shorts.

## What is this project?
The goal of this project is to create an automated pipeline that can take a broad topic and break it down into a production-ready YouTube Short concept. It achieves this by delegating different parts of the creative process to specialized sub-agents.

## ADK Features Used

This project utilizes several key components from the Google ADK:

### 1. Models (`google.adk.models`)
- **`Gemini`**: The project uses the `gemini-3.5-flash` model as the underlying intelligence for all the agents, connected via the `google.genai` enterprise client.

### 2. Agents (`google.adk.agents`)
- **`LlmAgent`**: Used to create specialized, single-purpose agents. We define three distinct LLM agents:
  - `ShortScriptWriter`: Responsible for generating the script for the short.
  - `ShortsVizualizer`: Responsible for generating visual concepts to accompany the script.
  - `ConceptFormatter`: Responsible for combining the script and visual concepts into a final, structured format.
- **`LoopAgent`**: Used for orchestration. The `youtube_shorts_agent` is a `LoopAgent` that coordinates the execution of the three sub-agents in a loop for a defined number of iterations (`max_iterations=3`).

### 3. Tools (`google.adk.tools`)
- **`google_search`**: The `ShortScriptWriter` agent is equipped with the `google_search` tool, allowing it to browse the web for up-to-date information and trends to write relevant scripts.

### 4. State Management
- **`output_key`**: The project demonstrates passing information between agents using state keys (e.g., `generated_script`, `visual_concepts`). The output of one agent is saved to the state and then accessed by downstream agents (like the `ConceptFormatter`).

## Project Structure
- `agent.py`: The main file where the Gemini model, tools, and all the ADK agents (`LlmAgent` and `LoopAgent`) are defined and wired together.
- Instructions: The project separates agent prompts into text files (e.g., `scriptwriter_instruction.txt`, `visualizer_instruction.txt`) which are loaded dynamically.

## Learning Objectives Achieved
- Setting up the GenAI client and initializing an ADK `Gemini` model.
- Creating multiple specialized `LlmAgent` instances with distinct personas and instructions.
- Equipping an agent with external capabilities using ADK Tools (`google_search`).
- Passing context between agents using `output_key`.
- Orchestrating a sequential multi-agent workflow using `LoopAgent`.
