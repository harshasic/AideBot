import google.generativeai as genai

API_KEY = " " # <Your api key here>

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("You are talking with your new AI helper AideBot. Press Ctrl + C to end the chat or type 'exit'")

while True:
    user_in = input("You: ")
    if user_in.lower() == 'exit':
        break
    response = chat.send_message(user_in)
    print(response.text)
    print(" " * 20)
