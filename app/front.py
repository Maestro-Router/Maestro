import time
import gradio as gr
from maestro import Maestro

from execute_backend import estimate_consumption

def echo_multimodal(message, history):
    response = []
    response.append("You wrote: '" + message["text"] + "' and uploaded:")
    if message.get("files"):
        for file in message["files"]:
            response.append(gr.File(value=file))
    return response


# Fonction de fallback
def general_fallback(prompt):
    return f"[Fallback] Je ne sais pas exactement quel modèle utiliser pour: {prompt}"


maestro = Maestro()

def send(message, history):
    # Obtain the raw response from Maestro (currently a simple string)
    # raw_response = maestro.handle_request(message, fallback_fn=general_fallback)

    # Simple mock token estimation (rough heuristic):
    # Use number of whitespace-separated words * 1.3 as pseudo token count.
    word_count = len(str(message).split())
    token_nb = int(word_count * 1.3)

    consumption = estimate_consumption(token_nb=token_nb)

    # Build consumption display including token count
    parts = [
        f"🌱 CO2: {consumption['co2_emissions_g']} g CO2eq",
        f"⚡ Energy: {consumption['energy_consumption_wh']} Wh",
    ]
    if consumption.get("token_nb") is not None:
        parts.append(f"🧪 Tokens (mock): {consumption['token_nb']}")

    consumption_block = "\n\n__" + " | ".join(parts) + "__"
    return consumption_block

demo = gr.ChatInterface(
    fn=send,
    title="Maestro AI",
    type="messages",
    flagging_mode="manual",
    flagging_options=["Like", "Spam", "Inappropriate", "Other"],    
    cache_mode="eager",
    examples=["Je veux savoir plus sur ", "Bonjour, ", ""],
    run_examples_on_click=False,
    save_history=True,
    delete_cache=None,
    multimodal=True,
    theme="ocean"
)

# demo.saved_conversations.secret = "abcdefasd6200683922"
# demo.saved_conversations.storage_key = "_saved_conversations"

if __name__ == "__main__":
    demo.launch()
