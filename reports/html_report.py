from jinja2 import Template

def generate(results, path):
    template = Template("""
    <html><head><title>Dependency Scan Report</title></head><body>
    <h1>Vulnerability Report</h1>
    {% for item in results %}
      <h2>{{ item.name }} ({{ item.version }})</h2>
      <ul>
        {% for vuln in item.vulnerabilities %}
          <li><strong>{{ vuln.id }}</strong>: {{ vuln.summary }}</li>
        {% endfor %}
      </ul>
    {% endfor %}
    </body></html>
    """)
    with open(path, "w") as f:
        f.write(template.render(results=results))
