# 🔍 ResearchPilot AI

**Multi-Agent Research & Report Assistant powered by LangGraph**

ResearchPilot AI is a production-style **multi-agent AI system** that autonomously researches a user query, extracts relevant information, verifies claims across multiple sources, generates a structured research report, supports **Human-in-the-Loop (HITL)** approval, stores previous research in vector memory, and exports reports in multiple formats.

---

## 🚀 Features

* 🤖 Multi-Agent Architecture using LangGraph
* 🌐 Real-time Web Search (Tavily)
* 📑 Intelligent Content Extraction
* ✅ AI-based Fact Verification
* 📝 Structured Research Report Generation
* 👨‍💻 Human-in-the-Loop Approval Workflow
* 🧠 FAISS Vector Memory for Previous Research
* 📄 Export Reports to:

  * PDF
  * DOCX
  * Markdown
* ⚡ FastAPI Backend
* 🎨 Interactive Streamlit Dashboard

---

# 🏗️ Architecture

```
                    User Query
                         │
                         ▼
                Supervisor Workflow
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Researcher Agent   Extractor Agent   Fact Checker
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  Writer Agent
                         │
                         ▼
             Human Review (HITL)
                         │
               ┌─────────┴─────────┐
               ▼                   ▼
          Export Report      Save to Memory
```

---

# 🧠 Agent Workflow

### 🔎 Researcher Agent

* Searches the web using Tavily
* Collects trusted sources
* Stores research data

---

### 📄 Extractor Agent

* Scrapes article content
* Cleans extracted text
* Splits content into chunks

---

### ✅ Fact Checker Agent

* Extracts important claims
* Cross-verifies claims
* Assigns confidence score

---

### ✍️ Writer Agent

* Organizes verified information
* Generates a structured research report

---

### 👨‍💻 Human Review

* Manual approval step
* Supports revision requests
* Unlocks report export after approval

---

# 💻 Tech Stack

### AI Frameworks

* LangGraph
* LangChain

### LLM

* Groq (Llama 3.3 70B)

### Search

* Tavily API

### Backend

* FastAPI

### Frontend

* Streamlit

### Vector Database

* FAISS

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### Export

* ReportLab
* python-docx

---

# 📂 Project Structure

```
ResearchPilot-AI/

│── app/
│   ├── agents/
│   ├── api/
│   ├── config/
│   ├── graph/
│   ├── services/
│   └── tools/
│
│── streamlit_app/
│   ├── components/
│   └── ui.py
│
│── tests/
│
│── main.py
│── requirements.txt
│── README.md
```

---

# ⚙️ Installation

Clone repository

```bash
git clone https://github.com/ssr3112/Multi-Agent-ResearchPilot-AI.git
```

Go to project

```bash
cd Multi-Agent-ResearchPilot-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
TAVILY_API_KEY=your_key
GROQ_API_KEY=your_key
LANGCHAIN_API_KEY=your_key

MODEL_NAME=llama-3.3-70b-versatile
MAX_SEARCH_RESULTS=5
```

---

# ▶️ Run Backend

```bash
uvicorn main:app --reload
```

---

# ▶️ Run Streamlit

```bash
streamlit run streamlit_app/ui.py
```

---

# 📸 Demo

Add screenshots here after uploading.

Example:

```
assets/home.png

assets/report.png

assets/workflow.png
```

---

# 🔮 Future Improvements

* Multi-user authentication
* Persistent vector database
* Multi-document research
* Citation generation
* Research history dashboard
* Async agent execution
* Docker deployment
* Cloud deployment (Render + Streamlit Cloud)

---

# 👨‍💻 Author

**Sudhanshu Singh**

Computer Science Engineer (Data Science)

Interested in:

* AI Engineering
* Generative AI
* Agentic AI
* NLP
* Machine Learning
* LLM Applications

---

## ⭐ If you found this project useful, consider giving it a Star.
