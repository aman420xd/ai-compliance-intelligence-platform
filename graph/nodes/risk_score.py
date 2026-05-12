from graph.state import ComplianceState


SEVERITY_WEIGHTS = {
    "CRITICAL": 40,
    "HIGH": 25,
    "MEDIUM": 15,
    "LOW": 5
}


def risk_score_node(
    state: ComplianceState
):

    findings = state.get("findings", [])

    total_score = 0

    severity_counts = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }

    affected_pages = set()

    for finding in findings:

        severity = finding["severity"]

        total_score += SEVERITY_WEIGHTS.get(
            severity,
            0
        )

        severity_counts[severity] += 1

        affected_pages.add(
            str(finding["page"])
        )

    final_risk_score = min(
        total_score,
        100
    )

    summary = {
        "total_findings": len(findings),
        "severity_breakdown": severity_counts,
        "affected_pages": len(affected_pages),
        "risk_score": final_risk_score
    }

    return {
        "risk_score": final_risk_score,
        "summary": summary
    }