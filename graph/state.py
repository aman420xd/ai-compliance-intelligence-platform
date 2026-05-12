from typing import TypedDict, List, Dict


class ComplianceState(TypedDict):

    pdf_path: str

    pages: List[Dict]

    findings: List[Dict]

    compliance_rules: Dict

    risk_score: int

    summary: Dict

    final_report: str