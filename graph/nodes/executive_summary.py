from graph.state import ComplianceState
from utils.llm import llm


def executive_summary_node(state: ComplianceState):

    findings = state.get("findings", [])

    prompt = f"""
You are an enterprise compliance auditor.

Based on these findings, generate:
1. Executive summary
2. Overall compliance verdict
3. Key risks
4. Recommended actions

Keep it professional and concise.

Findings:
{findings}
"""

    response = llm.invoke(prompt)

    state["summary"]["executive_summary"] = response.content

    return state