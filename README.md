# 🏥 AI-Powered Medical Assistant Chatbot

> An intelligent healthcare assistant built using **Azure OpenAI**, **LangChain**, and **Streamlit** to provide context-aware medical conversations through natural language interaction.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)]()
[![Azure OpenAI](https://img.shields.io/badge/LLM-Azure%20OpenAI-blue)]()
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

---

## 📖 Overview

The **AI-Powered Medical Assistant Chatbot** is a Generative AI application designed to simulate intelligent healthcare conversations. The system uses **Azure OpenAI's language models** along with **LangChain orchestration** to understand user queries and generate context-aware responses.

The project demonstrates the practical use of:

- Large Language Models (LLMs)
- Prompt Engineering
- Conversational AI
- AI-powered healthcare assistance
- Secure API integration
- Interactive web interfaces

This project was developed to explore how modern AI systems can improve accessibility and user interaction in healthcare-related applications.

---

## ✨ Key Features

### 🤖 AI-Powered Conversations
- Understands natural language medical queries
- Generates intelligent and contextual responses
- Maintains conversational flow

### 🧠 Generative AI Integration
- Uses Azure OpenAI models
- Prompt-based response generation
- Dynamic content creation

### 🔗 LangChain Workflow
- Handles prompts and chains efficiently
- Improves response management
- Creates structured AI pipelines

### 💻 Interactive User Experience
- Built with Streamlit
- Responsive and clean interface
- Real-time interaction

### 🔐 Secure Configuration
- Environment variables for API keys
- Secure credential management using dotenv

---

## 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Frontend | Streamlit |
| AI Framework | LangChain |
| LLM Service | Azure OpenAI |
| Environment Management | dotenv |
| Version Control | Git & GitHub |

---

## 🏗 System Architecture

```text
User Query
     ↓
Streamlit Interface
     ↓
LangChain Processing
     ↓
Azure OpenAI API
     ↓
Response Generation
     ↓
Display Result to User
```

---

## 📂 Project Structure

```bash
Medical-ChatBot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── assets/
│
├── utils/
│
└── modules/
```

---

## ⚙️ Installation Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/gautam-rahul-09/Medical-ChatBot.git
```

Move to project directory:

```bash
cd Medical-ChatBot
```

---

### Step 2: Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure Environment Variables

Create a `.env` file:

```env
AZURE_OPENAI_API_KEY=your_api_key

AZURE_OPENAI_ENDPOINT=your_endpoint

AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name

OPENAI_API_VERSION=your_api_version
```

---

### Step 5: Run Application

```bash
streamlit run app.py
```

Open browser:

```bash
http://localhost:8501
```

---

## 🔍 Workflow

### User Interaction

1. User enters a healthcare-related query.
2. Streamlit captures the input.
3. LangChain processes the request.
4. Azure OpenAI generates contextual responses.
5. Results are displayed dynamically.

---

## 💡 Example Queries

```text
What are common symptoms of diabetes?

How can I improve sleep quality?

Explain high blood pressure.

What foods help boost immunity?

What causes headaches?
```

---

## 🎯 Learning Outcomes

This project helped strengthen practical understanding of:

- Generative AI applications
- Prompt Engineering
- LLM integration
- LangChain pipelines
- API handling
- Streamlit development
- Secure environment management

---

## 🚀 Future Enhancements

- Voice-based interaction
- Retrieval Augmented Generation (RAG)
- Medical PDF upload support
- Chat history storage
- Authentication system
- Multi-language support
- Doctor recommendation system
- Deployment using Docker and Cloud platforms

---

## ⚠️ Disclaimer

This application is intended solely for:

- Educational purposes
- AI experimentation
- Demonstrating Generative AI capabilities

This chatbot does **not** provide professional medical advice, diagnosis, or treatment.

Users should always consult qualified healthcare professionals for medical concerns.

---

## 👨‍💻 Author

**Gautam Rahul**

📧 Email: gautamrahul2905@gmail.com

🔗 LinkedIn:  
https://linkedin.com/in/gautam-rahul-65172224a

💻 GitHub:  
https://github.com/gautam-rahul-09

---

## 🌟 Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the repository

🤝 Connect with me

---

"Building intelligent systems through AI-driven innovation."
