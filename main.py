import google.generativeai as genai

API_KEY = "AIzaSyBBU2rzMXreeqlN5o79jdE05x0cJRpXQxw"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("You are talking with your new AI helper NIX. Press Ctrl + C to end the chat or type 'exit'")

while True:
    user_in = input("You: ")
    if user_in.lower() == 'exit':
        break
    response = chat.send_message(user_in)
    print(response.text)
    print(" " * 20)
