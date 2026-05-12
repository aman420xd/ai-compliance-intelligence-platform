from graph.state import ComplianceState
from utils.pdf_parser import extract_pdf_pages


def extract_pdf_node(state: ComplianceState):

    pdf_path = state["pdf_path"]

    pages = extract_pdf_pages(pdf_path)

    state["pages"] = pages

    return state