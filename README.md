# AI Compliance Intelligence Platform

An AI-powered PDF compliance scanning platform built using Streamlit, LangGraph, Claude AI, and PyMuPDF.

## Features

- PDF Upload Interface
- AI-Powered Compliance Analysis
- Parallel Multi-Agent LangGraph Workflow
- PII / GDPR Detection
- Confidential Information Detection
- UTF-8 Encoding Validation
- Abusive / Unlawful Content Detection
- Contract Compliance Validation
- Risk Scoring Engine
- AI Executive Summary Generation
- Downloadable Compliance Reports
- Persistent Report Metadata Storage

---

## Tech Stack

- Streamlit
- LangGraph
- LangChain
- Claude API
- PyMuPDF
- Plotly
- Pandas

---

## Workflow Architecture

```text
PDF Upload
    ↓
PDF Extraction
    ↓
Parallel Compliance Agents
    ├── PII / GDPR Detection
    ├── Confidential Detection
    ├── Encoding Validation
    ├── Abuse Detection
    └── Contract Compliance
            ↓
Risk Scoring
            ↓
AI Executive Summary
            ↓
Final Compliance Report
```

---

## Installation

```bash
git clone <repo-url>

cd project-name

pip install -r requirements.txt
```

Create `.env`

```env
ANTHROPIC_API_KEY=your_api_key
```

Run Application

```bash
streamlit run app.py
```

---

## Project Structure

```text
graph/
    nodes/
    workflow.py
    state.py

utils/
    pdf_parser.py
    llm.py
    regex_patterns.py

reports/
uploads/
```

---

## Future Improvements

- PDF Highlight Visualization
- Rule Management Dashboard
- PDF Report Export
- Compliance History Retrieval
- Advanced Governance Policies

---


---

## Live Demo

https://ai-compliance-intelligence-platform.onrender.com

---

## Deployment

The application is deployed on Render using:

- Streamlit frontend
- LangGraph orchestration
- Claude AI integration
- PyMuPDF for PDF processing
- Plotly analytics dashboard

---

## Notes

- Uploaded PDFs are processed securely during runtime
- Reports are generated dynamically
- Environment variables are managed securely on Render


## Author

Priyanshu Tomar