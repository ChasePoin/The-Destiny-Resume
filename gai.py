import google.generativeai as genai
import os

def configureAI():
    # uses key from environment variable labeled "GOOGLE_API_KEY"
    # configures the gemini api
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    return model


def sendPrompt(model: genai.GenerativeModel, prompt: str) -> str:
    return model.generate_content(prompt)