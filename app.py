import streamlit as st
from pdf_processor import extract_text_from_pdf
from workflow import compliance_pipeline

st.set_page_config(page_title="Compliance Checker Pipeline", layout="wide")

st.title("🚀 AI-Accelerated Compliance Pipeline")

# Sidebar for Compliance Rules (Fulfills: provision for updating rules via UI)
st.sidebar.header("⚙️ Compliance Configuration")
default_rules = """1. Document must contain a 'Confidentiality' clause.
2. The term 'Indemnity' must be clearly defined.
3. Applicable governing law must be stated."""

compliance_rules = st.sidebar.text_area("Edit Compliance Rules:", value=default_rules, height=200)

# Main UI for PDF Upload
st.subheader("1. Upload Document")
uploaded_file = st.file_uploader("Upload a PDF to check for compliance", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")
    
    if st.button("Run Compliance Check"):
        with st.spinner("Processing PDF and running LangGraph pipeline..."):
            
            # Extract Text
            pdf_bytes = uploaded_file.read()
            raw_text = extract_text_from_pdf(pdf_bytes)
            
            # Run LangGraph Pipeline
            initial_state = {
                "document_text": raw_text,
                "compliance_rules": compliance_rules,
                "analysis_report": ""
            }
            
            # Execute workflow
            result = compliance_pipeline.invoke(initial_state)
            
            # Display Report
            st.subheader("📋 Compliance Report")
            st.markdown(result["analysis_report"])
            
            # Download Button for the report
            st.download_button(
                label="Download Report as TXT",
                data=result["analysis_report"],
                file_name="compliance_report.txt",
                mime="text/plain"
            )