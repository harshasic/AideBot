# 🤖 AI Chat Help

**AI Chat Help** is a simple and powerful chatbot built with Google's Generative AI. It enables real-time natural language interactions using Google's cutting-edge language models. This project is ideal for developers looking to experiment with conversational AI or integrate intelligent chat features into their applications.

---

## ✨ Features

- Built with `google-generativeai` package
- Lightweight and easy to customize
- Supports conversational interaction with AI
- Ready to extend for APIs, GUI, or automation

---

## 📦 Installation

Install the required dependency:

```bash
pip install google-generativeai
```

🧠 How It Works
This project uses Google's Generative AI to process natural language inputs and return intelligent responses. The google-generativeai library makes it easy to send prompts and receive AI-generated replies.

🔑 Note: You will need an API key from Google AI Studio to use the model. Follow their documentation to generate and use your API key.


🛠 Usage
1. Clone the repository:
```
git clone https://github.com/harshasic/AideBot.git
cd ai-chat-help
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Create a .env file and add your API key:
```
API_KEY=your_google_api_key_here
```
4. Run the chatbot:
```
python chatbot.py
```
5. Start chatting:
```
You: Hello!
Bot: Hi there! How can I help you today?
```
📁 Project Structure
```
ai-chat-help/
├── chatbot.py          # Main Python script for the chatbot
├── requirements.txt    # Dependency list
├── .env                # Your secret API key (not tracked in Git)
└── README.md           # Project documentation
```
📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Powered by Google Generative AI

Python 3.8+

Inspired by the need for quick AI chat prototypes


