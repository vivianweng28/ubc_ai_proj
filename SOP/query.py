import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('PROJECT_API_KEY')
os.environ["API_KEY"] = API_KEY

genai.configure(api_key=os.environ["API_KEY"])


model = genai.GenerativeModel('gemini-1.5-flash-latest')
response = model.generate_content("")
print(response.text)