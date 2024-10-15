# api key: AIzaSyBxsrHn41VQiBGcbG3xojrD0wMC4uWZfnY

import google.generativeai as genai
import os

os.environ["API_KEY"] = 'AIzaSyBxsrHn41VQiBGcbG3xojrD0wMC4uWZfnY'
genai.configure(api_key=os.environ["API_KEY"])
datacollection

model = genai.GenerativeModel('gemini-1.5-flash-latest')
response = model.generate_content("")
print(response.text)