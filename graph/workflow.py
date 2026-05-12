from langgraph.graph import StateGraph, END

from graph.state import ComplianceState

from graph.nodes.extract_pdf import extract_pdf_node
from graph.nodes.pii_check import pii_check_node
from graph.nodes.confidential_check import confidential_check_node
from graph.nodes.encoding_check import encoding_check_node
from graph.nodes.abuse_check import abuse_check_node
from graph.nodes.contract_check import contract_check_node
from graph.nodes.risk_score import risk_score_node
from graph.nodes.executive_summary import executive_summary_node
from graph.nodes.generate_report import generate_report_node


workflow = StateGraph(ComplianceState)


# Nodes
workflow.add_node("extract_pdf", extract_pdf_node)

workflow.add_node("pii_check", pii_check_node)

workflow.add_node("confidential_check", confidential_check_node)

workflow.add_node("encoding_check", encoding_check_node)

workflow.add_node("abuse_check", abuse_check_node)

workflow.add_node("contract_check", contract_check_node)

workflow.add_node("risk_score", risk_score_node)

workflow.add_node("executive_summary", executive_summary_node)

workflow.add_node("generate_report", generate_report_node)


# Entry Point
workflow.set_entry_point("extract_pdf")


# Parallel Compliance Agents
workflow.add_edge("extract_pdf", "pii_check")

workflow.add_edge("extract_pdf", "confidential_check")

workflow.add_edge("extract_pdf", "encoding_check")

workflow.add_edge("extract_pdf", "abuse_check")

workflow.add_edge("extract_pdf", "contract_check")


# Aggregation
workflow.add_edge("pii_check", "risk_score")

workflow.add_edge("confidential_check", "risk_score")

workflow.add_edge("encoding_check", "risk_score")

workflow.add_edge("abuse_check", "risk_score")

workflow.add_edge("contract_check", "risk_score")


# Final Stages
workflow.add_edge("risk_score", "executive_summary")

workflow.add_edge("executive_summary", "generate_report")

workflow.add_edge("generate_report", END)


# Compile Workflow
compliance_workflow = workflow.compile()