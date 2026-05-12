from graph.state import ComplianceState


ABUSIVE_WORDS = [
    "damn",
    "stupid",
    "fraud",
    "illegal",
    "abuse",
    "corrupt"
]


def abuse_check_node(
    state: ComplianceState
):

    findings = []

    for index, page in enumerate(state["pages"]):

        page_text = page["text"].lower()

        for word in ABUSIVE_WORDS:

            if word in page_text:

                findings.append({
                    "type": "Abusive Content",
                    "severity": "Medium",
                    "page": index + 1,
                    "details": f"Detected abusive keyword: {word}"
                })

    return {
        "findings": findings
    }