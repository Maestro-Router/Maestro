import gradio as gr


def render():
    with gr.Tab("Concept"):
        gr.Markdown(
            """
            # Maestro AI - Concept Overview

            This page introduces the core idea behind Maestro:
            A task-routing AI system powered by semantic embeddings
            that figures out automatically which agent should handle
            each user request.
            """
        )
