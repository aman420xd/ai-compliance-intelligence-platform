from graph.state import ComplianceState


REQUIRED_CLAUSES = [
    "confidentiality",
    "indemnity",
    "governing law"
]


def contract_check_node(
    state: ComplianceState
):

    findings = []

    full_document = " ".join(
        [
            page["text"].lower()
            for page in state["pages"]
        ]
    )

    for clause in REQUIRED_CLAUSES:

        if clause not in full_document:

            findings.append({
                "page": "DOCUMENT_LEVEL",
                "type": "CONTRACT_COMPLIANCE",
                "severity": "HIGH",
                "issue": f"Missing required clause: {clause}"
            })

    return {
        "findings": findings
    }