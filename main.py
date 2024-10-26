import google.generativeai as genai

API_KEY = "AIzaSyBWGd2JcfCubuZ7tpw35olV3LjQUUoCK7M"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")

print(response.text)