import gradio as gr

from app.tabs.about import render as render_tab4
from app.tabs.chat import render as render_tab3
from app.tabs.concept import render as render_tab1
from app.tabs.tools_functions_agents import render as render_tab2

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
        render_tab3()
        render_tab1()
        render_tab2()
        render_tab4()

if __name__ == "__main__":
    demo.launch(
        favicon_path="assets/favicon.ico",
    )
