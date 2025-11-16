import gradio as gr

from app.tabs.about import render as render_about_tab
from app.tabs.chat import render as render_chat_tab
from app.tabs.tools_functions_agents import render as render_tools_functions_agents_tab

css = """
#favicon {
    display:none !important;
}
"""

with gr.Blocks(
    title="Maestro AI",
    css=css,
    theme="ocean",
) as demo:
    with gr.Tabs():
        render_chat_tab()
        render_tools_functions_agents_tab()
        render_about_tab()

if __name__ == "__main__":
    demo.launch()
