import xml.etree.ElementTree as ET

def get_dependencies():
    deps = []
    try:
        tree = ET.parse("pom.xml")
        root = tree.getroot()
        ns = {"m": "http://maven.apache.org/POM/4.0.0"}
        for dep in root.findall(".//m:dependency", ns):
            group_id = dep.find("m:groupId", ns).text
            artifact_id = dep.find("m:artifactId", ns).text
            version = dep.find("m:version", ns).text
            deps.append({"ecosystem": "Maven", "name": f"{group_id}:{artifact_id}", "version": version})
    except FileNotFoundError:
        pass
    return deps
