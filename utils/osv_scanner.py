import requests

def check_vulnerabilities(ecosystem, name, version):
    url = "https://api.osv.dev/v1/query"
    payload = {
        "package": {"ecosystem": ecosystem, "name": name},
        "version": version
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get("vulns", [])
    except Exception:
        pass
    return []
