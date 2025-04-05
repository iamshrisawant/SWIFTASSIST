import os
from dotenv import load_dotenv
import google.generativeai as genai
from core.language_detect import detect_language

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Start Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# Initial system prompt
system_prompt = (
    "You are a multilingual roadside assistant chatbot. "
    "Help users diagnose simple vehicle issues, provide repair tips, and suggest when to call a mechanic."
)
chat.send_message(system_prompt)

def roadside_chat(prompt: str) -> str:
    lang = detect_language(prompt)
    print(f"[🌍 Detected language: {lang}]")
    response = chat.send_message(prompt)
    return response.text
