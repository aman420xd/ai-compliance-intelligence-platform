from graph.state import ComplianceState


def generate_report_node(state: ComplianceState):

    findings = state.get("findings", [])

    summary = state.get("summary", {})

    report = []

    report.append("# AI Compliance Report\n")

    report.append("## Executive Summary\n")

    report.append(f"Overall Risk Score: {summary.get('risk_score', 0)}/100\n")

    report.append(f"Total Findings: {summary.get('total_findings', 0)}\n")

    report.append(f"Affected Pages: {summary.get('affected_pages', 0)}\n")

    report.append("\n## Severity Breakdown\n")

    severity_data = summary.get("severity_breakdown", {})

    for severity, count in severity_data.items():

        report.append(f"- {severity}: {count}\n")

    report.append("\n## Detailed Findings\n")

    if not findings:

        report.append("No compliance violations detected.\n")

    else:

        for idx, finding in enumerate(findings, start=1):

            report.append(f"\n### Finding {idx}\n")

            report.append(f"- Page: {finding['page']}\n")

            report.append(f"- Type: {finding['type']}\n")

            report.append(f"- Severity: {finding['severity']}\n")

            report.append(f"- Issue: {finding['issue']}\n")

            if "matches" in finding:

                report.append(f"- Matches: {finding['matches']}\n")

    final_report = "\n".join(report)

    state["final_report"] = final_report

    return state