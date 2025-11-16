import gradio as gr


def render():
    with gr.Tab("About"):

        gr.Markdown(
            """
            # About Maestro

            Maestro is an intelligent multi-agent router that selects
            the best task model to answer each prompt.
            This page gives general project information.
            """
        )
