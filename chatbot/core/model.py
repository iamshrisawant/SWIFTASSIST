import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def get_model():
    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel("gemini-1.5-flash")
