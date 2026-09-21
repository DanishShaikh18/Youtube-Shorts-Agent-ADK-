from google import genai
from google.adk.agents import LlmAgent, LoopAgent
from google.adk.models import Gemini
from google.adk.tools import google_search

from .util import load_instruction_from_file

client = genai.Client(
    enterprise=True,
    project="project-garden-505118",
    location="global",
)
vertex_model = Gemini(model="gemini-3.5-flash", client=client)

# --- Sub Agent 1: ScriptWriter ---
scriptwriter_agent = LlmAgent(
    name="ShortScriptWriter",
    model=vertex_model,
    instruction=load_instruction_from_file('scriptwriter_instruction.txt'),
    tools=[google_search],
    output_key="generated_script"
)

# --- Sub Agent 2: Visualizer --- 
visualizer_agent = LlmAgent(
    name="ShortsVizualizer",
    model=vertex_model,
    instruction=load_instruction_from_file("visualizer_instruction.txt"),
    output_key="visual_concepts"
)

# --- Sub Agent 3: Formatter ---
formatter_agent = LlmAgent(
    name="ConceptFormatter",
    model=vertex_model,
    instruction="Combine the script of from state[generated_script] and the visual concepts from state[visual_concepts] into a structured format suitable for YouTube Shorts video production.",
    output_key="final_short_concept"
) 

#---LLM Agent ----
youtube_shorts_agent = LoopAgent(
    name = "youtube_shorts_agent",
    max_iterations=3,
    sub_agents = [
        scriptwriter_agent, 
        visualizer_agent,
        formatter_agent
    ]
)

root_agent = youtube_shorts_agent