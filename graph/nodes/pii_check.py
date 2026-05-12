import re

from graph.state import ComplianceState

from utils.regex_patterns import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    AADHAAR_PATTERN,
    PAN_PATTERN,
    CREDIT_CARD_PATTERN
)


def pii_check_node(state: ComplianceState):

    findings = []

    for page in state["pages"]:

        text = page["text"]

        checks = [
            ("Email detected", EMAIL_PATTERN, "HIGH"),
            ("Phone number detected", PHONE_PATTERN, "MEDIUM"),
            ("Aadhaar number detected", AADHAAR_PATTERN, "CRITICAL"),
            ("PAN card detected", PAN_PATTERN, "HIGH"),
            ("Credit card detected", CREDIT_CARD_PATTERN, "CRITICAL")
        ]

        for issue_name, pattern, severity in checks:

            matches = re.findall(pattern, text)

            if matches:

                findings.append({
                    "page": page["page"],
                    "type": "PII",
                    "severity": severity,
                    "issue": issue_name,
                    "matches": matches
                })

    return {
        "findings": findings
    }