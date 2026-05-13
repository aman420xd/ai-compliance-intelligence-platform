# 🛡 AI Compliance Intelligence Platform

An AI-powered compliance analysis platform built using Streamlit, LangGraph, Groq LLMs, and Supabase.

This platform allows users to upload PDF documents and automatically analyze them for:

- Personally Identifiable Information (PII)
- Confidential content
- Contract compliance issues
- Encoding anomalies
- Abusive or risky language
- AI-generated executive summaries
- Risk scoring and compliance reporting

---

# 🚀 Live Demo

Add your deployed Render URL here:

```bash
https://ai-compliance-intelligence-platform.onrender.com/
```

---

# ✨ Features

## 📄 PDF Upload & Parsing
- Upload PDF documents through Streamlit UI
- Extracts page-wise text using PyMuPDF

## 🔍 Compliance Checks

### PII Detection
Detects:
- Emails
- Phone numbers
- Aadhaar numbers
- PAN numbers
- Credit card numbers

### Confidential Information Detection
Detects keywords like:
- Confidential
- Internal
- Proprietary
- Secret

### Contract Compliance Validation
Checks for required clauses:
- Confidentiality
- Indemnity
- Governing Law

### Encoding Validation
Detects:
- UTF-8 encoding issues
- Unsupported characters

### Abusive/Risky Content Detection
Detects risky or abusive keywords.

---

# 🤖 GenAI Integration

The platform uses:

- Groq API
- Llama 3.1 model
- LangChain
- LangGraph

for generating:
- AI executive summaries
- Compliance insights
- Risk explanations
- Recommended actions

---

# 📊 Dashboard Analytics

The application provides:

- Risk score visualization
- Severity breakdown charts
- Findings tables
- Executive summaries
- Downloadable compliance reports

---

# ☁ Cloud Architecture

## Frontend
- Streamlit

## Workflow Orchestration
- LangGraph

## LLM Framework
- LangChain

## AI Provider
- Groq

## Cloud Storage
- Supabase Storage

## Deployment
- Render

---

# 🧠 LangGraph Workflow

The compliance workflow contains multiple nodes:

1. Extract PDF
2. PII Check
3. Confidential Check
4. Contract Compliance Check
5. Encoding Validation
6. Abuse Detection
7. Risk Score Calculation
8. Executive Summary Generation
9. Report Generation

Parallel processing is used for compliance checks.

---

# 📂 Project Structure

```bash
ai-compliance-intelligence-platform/
│
├── app.py
├── requirements.txt
├── .env
│
├── graph/
│   ├── workflow.py
│   ├── state.py
│   └── nodes/
│       ├── extract_pdf.py
│       ├── pii_check.py
│       ├── confidential_check.py
│       ├── contract_check.py
│       ├── encoding_check.py
│       ├── abuse_check.py
│       ├── risk_score.py
│       ├── executive_summary.py
│       └── generate_report.py
│
├── utils/
│   ├── llm.py
│   ├── pdf_parser.py
│   ├── regex_patterns.py
│   ├── storage.py
│   ├── supabase_client.py
│   └── report_storage.py
│
├── uploads/
└── reports/
```

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/aman420xd/ai-compliance-intelligence-platform.git
```

```bash
cd ai-compliance-intelligence-platform
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

---

# ▶ Running Locally

```bash
streamlit run app.py
```

---

# ☁ Deployment

The application is deployed using:

- GitHub
- Render
- Supabase

## Render Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

# 📸 Screenshots

Add screenshots here:

- Dashboard
- Upload UI
- Findings Table
- Risk Analytics
- Executive Summary

---

# 🔒 Compliance Use Cases

This platform can be used for:

- Enterprise document compliance
- Legal contract review
- Sensitive information auditing
- Internal policy validation
- AI governance workflows
- Security audits

---

# 📈 Future Improvements

Potential future enhancements:

- Multi-file batch processing
- Vector database integration
- RAG-based compliance reasoning
- OCR support
- User authentication
- Report persistence in Supabase
- Advanced AI remediation suggestions
- Multi-tenant architecture

---

# 🛠 Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend |
| Streamlit | Frontend UI |
| LangGraph | Workflow orchestration |
| LangChain | LLM integration |
| Groq | AI inference |
| Supabase | Cloud storage |
| Plotly | Visualization |
| PyMuPDF | PDF parsing |
| Render | Deployment |

---

# 👨‍💻 Author

Aman

GitHub:

https://github.com/aman420xd

---

# 📜 License

This project is built for educational and portfolio purposes.

