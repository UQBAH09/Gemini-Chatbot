# Genimai Chatbot

Genimai Chatbot is a web-based conversational assistant powered by Google's Generative AI and built using **FastAPI** for the backend and standard HTML/CSS/JavaScript for the frontend. It provides a simple, interactive interface for chatting with an AI assistant.

## 🚀 Features

- 🌐 RESTful API built with FastAPI
- 🤖 Chatbot powered by Google's Generative AI
- 🌱 Environment-based configuration with `.env`
- 🔧 Easy to deploy and customize
- 🧠 Frontend included (HTML/CSS/JS)

## 🛠️ Tech Stack

- **Backend:** FastAPI, Pydantic
- **AI Model:** Google Generative AI (`google-generativeai`)
- **Environment Config:** python-dotenv
- **Frontend:** HTML, CSS, JavaScript

## 📁 Project Structure

```
Genimai chatbot/
├── app/
│   ├── main.py          # FastAPI app and endpoints
│   ├── chatbot.py       # Core chatbot logic using Google Generative AI
│   ├── config.py        # Environment/config setup
│   └── __init__.py
├── frontend/
│   ├── index.html       # Frontend interface
│   ├── main.js
│   └── style.css
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md
```

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/genimai-chatbot.git
   cd genimai-chatbot
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and set your API key:**
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000
   ```

## 🔒 Environment Variables

Make sure your `.env` file includes the following:

```env
GOOGLE_API_KEY=your_google_api_key
```

## 🧪 API Endpoints

| Method | Endpoint    | Description        |
|--------|-------------|--------------------|
| POST   | `/chat`     | Send user prompt and receive AI response |


Made with ❤️ using FastAPI + GenAI
