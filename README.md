# 🤖 AI Nexus Studio – Multi-AI Copilot Platform

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange?logo=google)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-yellow)
![Sentence Transformers](https://img.shields.io/badge/Sentence--Transformers-NLP-purple)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-blue?logo=plotly)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)
![dotenv](https://img.shields.io/badge/dotenv-Environment%20Variables-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

**AI Nexus Studio** is a **multi-AI assistant platform** that integrates several intelligent copilots into a single application.

The platform allows users to **research topics, generate code, analyze datasets, understand images, and interact with an AI chatbot** through one unified interface.

This project demonstrates a **real-world Generative AI application architecture** using modern AI tools and production-ready development practices.

---

# 🚀 Live Demo

Try the deployed application:

🔗 **Streamlit App**
https://ai-nexus-studio.streamlit.app/

---

# 🧠 AI Copilots Included

AI Nexus Studio provides **five intelligent AI tools**:

### 🔎 Research Nexus

AI-powered research assistant that generates structured explanations and summaries for any topic.

### 💻 Coding Nexus

Generates code, explains programming concepts, and helps debug problems using AI.

### 📊 Data Analysis Nexus

Upload CSV datasets and generate insights, statistics, and quick visual exploration.

### 🖼 Image Analysis Nexus

Analyzes uploaded images using **computer vision models** to identify objects and visual elements.

### 💬 Knowledge Chatbot

Conversational AI assistant powered by **Google Gemini** for answering questions and learning topics.

---

# ✨ Key Features

✔ Multi-AI Copilot platform
✔ Google Gemini LLM integration
✔ Computer Vision image analysis
✔ CSV dataset insights with Pandas
✔ Modern Streamlit user interface
✔ Secure API key handling with `.env`
✔ Modular architecture for scalability

---

# 🏗️ Project Architecture

```
ai-nexus-studio
│
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
├── .env.example
│
├── assets
│   ├── logo.png
│   └── background.png
│
├── modules
│   ├── research_nexus.py
│   ├── coding_nexus.py
│   ├── data_nexus.py
│   ├── image_nexus.py
│   └── knowledge_chatbot.py
│
├── utils
│   ├── gemini_client.py
│   ├── ui_components.py
│   └── helpers.py
│
└── models
    └── image_classifier.py
```

---

# ⚙️ Tech Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Core backend language     |
| Streamlit             | Web application framework |
| Google Gemini API     | Generative AI models      |
| Transformers          | Image classification      |
| Sentence Transformers | Text embeddings           |
| Pandas                | Data analysis             |
| Plotly                | Data visualization        |
| SQLite                | Authentication database   |
| dotenv                | Secure API key management |

---

# 🔐 Environment Variables

Create a `.env` file in the root folder.

```
GEMINI_API_KEY=your_api_key_here
```

Never commit your API keys to GitHub.

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/22AD040/ai-nexus-studio.git
cd ai-nexus-studio
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# ☁️ Streamlit Cloud Deployment

1. Push project to GitHub
2. Go to

https://share.streamlit.io

3. Select repository
4. Set main file:

```
app.py
```

5. Add **Secrets**:

```
GEMINI_API_KEY = "your_api_key"
```

---

# 📊 Example Use Cases

AI Nexus Studio can be used for:

• AI-assisted research
• Coding help and debugging
• Dataset exploration and insights
• Image recognition and classification
• General knowledge AI chatbot

---

# 🎯 Learning Outcomes

This project demonstrates skills in:

• Generative AI integration
• LLM application development
• AI system architecture
• Authentication systems
• AI-driven UI design
• End-to-end AI product development

---

# 📌 Future Improvements

Possible upgrades:

• Vector database search (RAG)
• PDF question answering
• Chat history storage
• AI document summarization
• Multi-modal AI pipelines
• Advanced analytics dashboards

---

# 👩‍💻 Author

**Ratchita B**

AI / Machine Learning Enthusiast
Building intelligent AI applications with Generative AI and ML.

GitHub:
https://github.com/22AD040

---

# 📜 License

This project is licensed under the **MIT License**.
