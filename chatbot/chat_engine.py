# chatbot/chat_engine.py

from core.language_detect import detect_language
from core.model import get_model
from core.prompts import BASE_PROMPT
from utils.formatters import format_gemini_response


# Rename this
async def generate_response(message: str) -> str:
    lang = detect_language(message)
    prompt = f"{BASE_PROMPT}\nUser: {message}\nAssistant:"

    try:
        model = get_model()
        response = await model.generate_content_async(prompt)
        raw_text = response.text.strip()
        formatted_html = format_gemini_response(raw_text)
        return formatted_html
    except Exception as e:
        print("Model error:", e)
        return "<p>Sorry, I'm having trouble responding right now.</p>"

