import gradio as gr
from agent.agent_main import run_agent

def chat(user_input):
    return run_agent(user_input)

gr.Interface(fn=chat, inputs="text", outputs="text", title="LangChain Agent").launch()