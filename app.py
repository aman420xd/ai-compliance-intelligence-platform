import os

import pandas as pd
import plotly.express as px
import streamlit as st

from graph.workflow import compliance_workflow
from utils.report_storage import save_report
 # from utils.storage import upload_pdf_to_supabase


st.set_page_config(
    page_title="AI Compliance Intelligence Platform",
    layout="wide"
)


st.title("🛡 AI Compliance Intelligence Platform")

st.markdown(
    "Upload PDF documents for AI-powered compliance analysis."
)


uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:

        f.write(uploaded_file.read())

    cloud_file_url = upload_pdf_to_supabase(
     pdf_path,
      uploaded_file.name
    )

    st.success("PDF uploaded successfully.")

    st.markdown(f"Cloud Storage Upload Complete")

    if st.button("Run Compliance Analysis"):

        with st.spinner("Running AI compliance workflow..."):

            initial_state = {
                "pdf_path": pdf_path,
                "pages": [],
                "findings": [],
                "compliance_rules": {},
                "risk_score": 0,
                "summary": {},
                "final_report": ""
            }

            result = compliance_workflow.invoke(initial_state)

            save_report(
                uploaded_file.name,
                result["final_report"],
                result["summary"]
            )

            findings = result["findings"]

            summary = result["summary"]

            st.subheader("📊 Risk Overview")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Risk Score",
                f"{summary.get('risk_score', 0)}/100"
            )

            col2.metric(
                "Total Findings",
                summary.get("total_findings", 0)
            )

            col3.metric(
                "Affected Pages",
                summary.get("affected_pages", 0)
            )

            st.subheader("📈 Severity Breakdown")

            severity_data = summary.get(
                "severity_breakdown",
                {}
            )

            severity_df = pd.DataFrame({
                "Severity": list(severity_data.keys()),
                "Count": list(severity_data.values())
            })

            fig = px.bar(
                severity_df,
                x="Severity",
                y="Count",
                title="Compliance Findings by Severity"
            )

            st.plotly_chart(fig)

            st.subheader("📋 Findings Table")

            if findings:

                findings_df = pd.DataFrame(findings)

                st.dataframe(findings_df)

            st.subheader("🧠 AI Executive Summary")

            st.markdown(
                summary.get(
                    "executive_summary",
                    "No summary generated."
                )
            )

            st.subheader("📄 Final Compliance Report")

            st.markdown(result["final_report"])

            st.download_button(
                label="Download Report",
                data=result["final_report"],
                file_name="compliance_report.txt",
                mime="text/plain"
            )