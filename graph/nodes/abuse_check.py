from graph.state import ComplianceState
from utils.llm import llm


def abuse_check_node(state: ComplianceState):

    findings = state.get("findings", [])

    for page in state["pages"]:

        text = page["text"]

        prompt = f"""
You are a compliance moderation system.

Analyze the following content.

Check whether it contains:
- abusive language
- hate speech
- threats
- unlawful or illegal content
- harassment
- toxic language

Return ONLY:
YES - if abusive/unlawful content exists
NO - if clean

Page Content:
{text}
"""

        response = llm.invoke(prompt)

        result = response.content.strip()

        if "YES" in result.upper():

            findings.append({
                "page": page["page"],
                "type": "ABUSIVE_CONTENT",
                "severity": "HIGH",
                "issue": "Abusive or unlawful content detected"
            })

    state["findings"] = findings

    return state