import gradio as gr
import openai
import os 

openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

def get_groq_response(message):
  try:
    response = openai.ChatCompletion.create(
        model = "llama-3.1-70b-versatile",
        messages = [
            {"role": "system", "content": "You will only answer in Hindi"},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message["content"]
  except Exception as e:
    return f"Error: {str(e)}" 

def chatbot(user_input, history = []):
  bot_response = get_groq_response(user_input)
  history.append((user_input, bot_response))
  return history, history

chat_interface = gr.Interface(
    fn=chatbot,
    inputs= ["text", "state"],
    outputs=["chatbot", "state"],
    live=False,
    title="My Chatbot",
    description="Mom: We have ChatGPT at Home, \n ChatGPT at Home:"
)
chat_interface.launch()
