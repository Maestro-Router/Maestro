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


total_watt_hours = 0.0  # Watt-hours (Wh)
total_co2_grams = 0.0   # Grams of CO2



def render():
    with gr.Tab("Chat"):
        feedback_log = {}

        def calculate_energy_impact(message, response):

            # Estimate tokens (rough approximation: 1 word ≈ 1.3 tokens)
            input_tokens = len(message.split()) * 1.3
            output_tokens = len(response.split()) * 1.3
            total_tokens = input_tokens + output_tokens

            # Energy consumption: approximately 0.001 Wh per 100 tokens (conservative estimate)
            # This is based on research showing GPT-3 uses about 1-5 Wh per 1000 tokens
            watt_hours = (total_tokens / 100) * 0.001
            watt_hours = max(0.002, min(watt_hours, 0.030))  # Clamp between 2-30 milliwatt-hours

            # CO2 emissions: average global grid intensity is ~475g CO2/kWh
            # Convert Wh to kWh and multiply by CO2 intensity
            co2_grams = (watt_hours / 1000) * 475

            return watt_hours, co2_grams



        with gr.Row():
            watt_display = gr.Textbox(
                value="⚡ Energy: 0.000 Wh",
                label="Total Energy Consumption",
                interactive=False,
                scale=1
            )
            co2_display = gr.Textbox(
                value="🌍 CO2: 0.000 g",
                label="Total CO2 Emissions",
                interactive=False,
                scale=1
            )

        # Chat interface
        chatbot = gr.Chatbot(type="messages", height=400)

        # Feedback display
        feedback_display = gr.Textbox(
            label="Feedback Log",
            value="",
            interactive=False,
            visible=False,
            max_lines=3
        )

        # Message input with file upload button on the side
        with gr.Row():
            msg = gr.Textbox(
                label="Your message",
                placeholder="Type your message here...",
                show_label=False,
                container=False,
                scale=10
            )
            file_upload = gr.UploadButton(
                "📎",
                file_count="multiple",
                # file_types=[".txt", ".pdf", ".doc", ".docx", ".csv", ".json", ".py", ".md", ".jpg", ".jpeg", ".png", ".mp3", ".wav"],
                scale=0,
                size="lg"
            )

        # Buttons below the text input
        with gr.Row():
            submit = gr.Button("Send", variant="primary", scale=1)
            clear = gr.Button("Clear", scale=1)


        gr.Examples(
            examples=[
                "Qui a développé Maestro ?",
                "Comment fonctionne ton routage ?",
                "Qui va gagner le Hackathon ?",
                "Quels sont tes agents ?",
                "Pourquoi ce nom ?",
                "En quoi es-tu frugale ?",
                "..."
            ],
            inputs=msg
        )

        def respond(message, chat_history, files):
            global total_watt_hours, total_co2_grams

            if not message.strip():
                return "", chat_history, f"⚡ Energy: {total_watt_hours:.3f} Wh", f"🌍 CO2: {total_co2_grams:.3f} g", None, gr.update(visible=False), ""

            # Build the full message with file information
            full_message = message
            user_display_message = message

            # Only process files if they exist
            if files:
                file_info = "\n\n📎 Attached files:\n"
                for file in files:
                    if hasattr(file, 'name'):
                        file_path = file.name if hasattr(file, 'name') else str(file)
                        file_info += f"- {file_path}\n"
                        print(f"📎 Attachment location: {file_path}")
                    else:
                        file_info += f"- {str(file)}\n"
                        print(f"📎 Attachment location: {str(file)}")
                full_message += file_info
                user_display_message += file_info

            # Get response
            bot_message = send(full_message, chat_history, attachments=files)

            maestro_file = "Type de fichier non reconnu"
            if files:
                if "." in files[0].name:
                    user_file_lower = "." + files[0].name.lower().split(".")[-1]
                else:
                    user_file_lower = ""

            # Detectar tipo de archivo
                img_extensions = (".jpg", ".jpeg", ".png")
                file_extensions = (".pdf", ".txt")
                audio_extensions = (".wav", ".mp3")

                if user_file_lower in img_extensions:
                    maestro_file = "Fichier a retourner : Image"
                elif user_file_lower in file_extensions:
                    maestro_file = "Fichier a retourner : Texte"
                elif user_file_lower in audio_extensions:
                    maestro_file = "Fichier a retourner : Audio"

            # Concatenar info al mensaje
            bot_message += " | " + maestro_file


            # Calculate realistic energy impact
            watt_hours, co2_grams = calculate_energy_impact(full_message, bot_message)

            # Increment counters
            total_watt_hours += watt_hours
            total_co2_grams += co2_grams

            # Update chat history
            chat_history.append({"role": "user", "content": user_display_message})
            chat_history.append({"role": "assistant", "content": bot_message})

            # Update counters display with realistic units
            watt_text = f"⚡ Energy: {total_watt_hours:.3f} Wh"
            co2_text = f"🌍 CO2: {total_co2_grams:.3f} g"

            # Clear the message input, update chat, update counters, and clear files
            return "", chat_history, watt_text, co2_text, None, gr.update(visible=False), ""

        def handle_like_event(data: gr.LikeData):
            """Handle like/dislike - show feedback in a display"""
            global feedback_log

            message_id = data.index
            feedback_type = "👍 Liked" if data.liked else "👎 Disliked"

            # Store feedback
            feedback_log[message_id] = feedback_type

            # Print to console with more detail
            print(f"\n{'='*50}")
            print(f"{feedback_type} message at index: {message_id}")
            print(f"Message content: {data.value}")
            print(f"{'='*50}\n")

            # Create feedback summary
            feedback_text = f"{feedback_type} message #{message_id}"

            return gr.update(visible=True, value=feedback_text)

        def reset_counters():
            global total_watt_hours, total_co2_grams, feedback_log
            total_watt_hours = 0.0
            total_co2_grams = 0.0
            feedback_log = {}
            return [], "⚡ Energy: 0.000 Wh", "🌍 CO2: 0.000 g", None, gr.update(visible=False), ""

        # Event handlers
        submit.click(
            respond,
            inputs=[msg, chatbot, file_upload],
            outputs=[msg, chatbot, watt_display, co2_display, file_upload, feedback_display, feedback_display]
        )

        msg.submit(
            respond,
            inputs=[msg, chatbot, file_upload],
            outputs=[msg, chatbot, watt_display, co2_display, file_upload, feedback_display, feedback_display]
        )

        clear.click(
            reset_counters,
            outputs=[chatbot, watt_display, co2_display, file_upload, feedback_display, feedback_display]
        )

        # Like/Dislike handler - show feedback in display
        chatbot.like(
            handle_like_event,
            inputs=None,
            outputs=[feedback_display]
        )
