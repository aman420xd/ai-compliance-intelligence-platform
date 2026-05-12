from graph.state import ComplianceState


CONFIDENTIAL_KEYWORDS = [
    "confidential",
    "internal",
    "secret",
    "proprietary",
    "private",
    "restricted"
]


def confidential_check_node(
    state: ComplianceState
):

    findings = []

    for page in state["pages"]:

        page_text = page["text"].lower()

        for keyword in CONFIDENTIAL_KEYWORDS:

            if keyword in page_text:

                findings.append({
                    "type": "Confidential Information",
                    "severity": "High",
                    "page": page["page_number"],
                    "details": f"Detected keyword: {keyword}"
                })

    return {
        "findings": findings
    }