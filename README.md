# py-dep-vuln-check

A multi-language dependency vulnerability scanner using OSV.dev. Supports Python, npm, and Maven projects.

## Features
- Scans `requirements.txt`, `package-lock.json`, and `pom.xml`
- Checks for known vulnerabilities via OSV.dev
- Generates HTML, JSON, and XML reports
- Supports suppression of known CVEs
- GitHub Actions integration

## Usage
```bash
python scanner.py
