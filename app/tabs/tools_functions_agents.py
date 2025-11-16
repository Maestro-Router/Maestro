import gradio as gr

from app.maestro import maestro


def render():
    with gr.Tab("Available Tasks"):

        try:
            items = []
            for t in maestro.tasks:
                name = getattr(t, "task", t).value if hasattr(t, "task") else getattr(t, "name", str(t))
                desc = getattr(t, "description", "")
                items.append(f"### **{name}**\n{desc}\n")

            gr.Markdown("\n".join(items))

        except Exception:
            gr.Markdown("Unable to load tasks.")
