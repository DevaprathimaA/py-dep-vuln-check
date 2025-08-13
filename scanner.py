import os
from parsers import python_parser, npm_parser, maven_parser
from reports import html_report, json_report, xml_report
from utils import osv_scanner, suppressor

def scan_project():
    all_dependencies = []

    # Parse dependencies
    all_dependencies += python_parser.get_dependencies()
    all_dependencies += npm_parser.get_dependencies()
    all_dependencies += maven_parser.get_dependencies()

    # Load suppressions
    suppressed_ids = suppressor.load_suppressions()

    results = []
    for dep in all_dependencies:
        vulns = osv_scanner.check_vulnerabilities(dep["ecosystem"], dep["name"], dep["version"])
        filtered = [v for v in vulns if v["id"] not in suppressed_ids]
        if filtered:
            results.append({**dep, "vulnerabilities": filtered})

    # Generate reports
    os.makedirs("reports_output", exist_ok=True)
    html_report.generate(results, "reports_output/report.html")
    json_report.generate(results, "reports_output/report.json")
    xml_report.generate(results, "reports_output/report.xml")

    print(f"✅ Scan complete. {len(results)} vulnerable packages found.")
    print("📄 Reports saved in reports_output/")

if __name__ == "__main__":
    scan_project()
