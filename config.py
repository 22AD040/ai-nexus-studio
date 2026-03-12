import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please set environment variable.")

genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(prompt):

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"⚠️ Gemini API Error: {str(e)}"