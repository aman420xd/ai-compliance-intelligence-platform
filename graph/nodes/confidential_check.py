from graph.state import ComplianceState
from utils.llm import llm


def confidential_check_node(state: ComplianceState):

    findings = state.get("findings", [])

    for page in state["pages"]:

        text = page["text"]

        prompt = f"""
You are a compliance auditor.

Analyze the following page content.

Detect whether it contains:
- confidential company information
- proprietary business logic
- internal architecture details
- trade secrets
- intellectual property sensitive content

Return ONLY:
YES - if confidential content exists
NO - if clean

Page Content:
{text}
"""

        response = llm.invoke(prompt)

        result = response.content.strip()

        if "YES" in result.upper():

            findings.append({
                "page": page["page"],
                "type": "CONFIDENTIAL",
                "severity": "HIGH",
                "issue": "Confidential information detected"
            })

    state["findings"] = findings

    return state
    