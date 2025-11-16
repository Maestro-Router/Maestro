import gradio as gr
from maestro import maestro
from app.logging_utils import get_logger

logger = get_logger(__name__)

def general_fallback(prompt):
    return "I'm sorry, I don't have the information to answer that question right now."

def send(message, history, attachments=None):
    logger.info(f"Received message: {message}")
    logger.debug(f"Current history: {history}")
    logger.debug(f"Current attachments: {attachments}")

    return maestro.handle_request(message, fallback_fn=general_fallback)


# TODO: if possible, return different examples at each call. FYI, gradio loads them only once at startup.
def get_examples() -> list[str]:
    return [
        "Qui a développé Maestro ?",
        "Comment fonctionne ton routage ?",
        "Qui va gagner le Hackathon ?",
        # "Quels sont tes agents ?",
        # "Pourquoi ce nom ?",
        # "En quoi es-tu frugale ?",
    ]



def render():
    with gr.Tab("Chat"):
        gr.ChatInterface(
            fn=send,
            # title="Maestro AI",
            # description="Chat with the Maestro engine.",
            type="messages",
            flagging_mode="manual",
            editable=True,
            flagging_options=["Like", "Spam", "Inappropriate", "Other"],
            cache_mode="eager",
            examples=get_examples(),
            run_examples_on_click=False,
            save_history=True,
            delete_cache=None,
            multimodal=True,
            theme="ocean"
        )
