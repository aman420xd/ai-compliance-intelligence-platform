from typing import TypedDict, List, Dict, Annotated
import operator


class ComplianceState(TypedDict):

    pdf_path: str

    pages: List[Dict]

    findings: Annotated[List[Dict], operator.add]

    compliance_rules: Dict

    risk_score: int

    summary: Dict

    final_report: str