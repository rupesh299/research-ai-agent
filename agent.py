import os
import google.generativeai as genai
from dotenv import load_dotenv
from tools import search_web

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-3.5-flash")

def research(topic):

    search_results = search_web(topic)

    prompt = f"""
    You are a research assistant.

    Topic:
    {topic}

    Search Results:
    {search_results}

    Write a professional report with:

    1. Overview
    2. Key Findings
    3. Current Trends
    4. Conclusion
    """

    response = model.generate_content(prompt)

    return response.text