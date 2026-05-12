from graph.state import ComplianceState


def encoding_check_node(state: ComplianceState):

    findings = state.get("findings", [])

    for page in state["pages"]:

        text = page["text"]

        try:

            text.encode("utf-8")

        except UnicodeEncodeError:

            findings.append({
                "page": page["page"],
                "type": "ENCODING",
                "severity": "MEDIUM",
                "issue": "UTF-8 encoding issue detected"
            })

            continue

        # English-only validation
        if not text.isascii():

            findings.append({
                "page": page["page"],
                "type": "ENCODING",
                "severity": "LOW",
                "issue": "Non-English or unsupported characters detected"
            })

    state["findings"] = findings

    return state