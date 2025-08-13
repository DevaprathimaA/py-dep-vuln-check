import xml.etree.ElementTree as ET

def generate(results, path):
    root = ET.Element("VulnerabilityReport")
    for item in results:
        pkg = ET.SubElement(root, "Package", name=item["name"], version=item["version"])
        for vuln in item["vulnerabilities"]:
            ET.SubElement(pkg, "Vulnerability", id=vuln["id"]).text = vuln["summary"]
    tree = ET.ElementTree(root)
    tree.write(path)
