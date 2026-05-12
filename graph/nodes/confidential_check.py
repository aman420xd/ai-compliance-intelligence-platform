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

    for index, page in enumerate(state["pages"]):

        page_text = page["text"].lower()

        for keyword in CONFIDENTIAL_KEYWORDS:

            if keyword in page_text:

                findings.append({
                    "type": "Confidential Information",
                    "severity": "High",
                    "page": index + 1,
                    "details": f"Detected keyword: {keyword}"
                })

    return {
        "findings": findings
    }