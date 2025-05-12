# Automated Reporting (Python)
import pandas as pd
from jinja2 import Template
from weasyprint import HTML
from sqlalchemy import create_engine

# Load data
engine = create_engine(conn)
df = pd.read_sql_table('etl_table', engine)

# Render template
tmpl = Template("""
<html><body>
  <h1>ETL Report</h1>
  <p>Records processed: {{count}}</p>
</body></html>
""")
html = tmpl.render(count=len(df))
HTML(string=html).write_pdf('report.pdf')
print('report.pdf generated')