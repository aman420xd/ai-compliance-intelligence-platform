import json
import os
from datetime import datetime


def save_report(
    filename,
    report_text,
    summary
):

    os.makedirs("reports", exist_ok=True)

    base_name = filename.replace(".pdf", "")

    report_path = f"reports/{base_name}_report.txt"

    metadata_path = f"reports/{base_name}_metadata.json"


    # Save report text
    with open(report_path, "w") as f:

        f.write(report_text)


    metadata = {
        "filename": filename,
        "risk_score": summary.get("risk_score", 0),
        "total_findings": summary.get("total_findings", 0),
        "affected_pages": summary.get("affected_pages", 0),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


    # Save metadata
    with open(metadata_path, "w") as f:

        json.dump(metadata, f, indent=4)