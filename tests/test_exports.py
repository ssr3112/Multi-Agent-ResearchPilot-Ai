# test_export.py

from app.tools.exporter import (
    export_pdf,
    export_docx,
    export_markdown
)

sample_report = """
# Research Report

AI Agent Frameworks are becoming
widely adopted.

LangGraph is among the leading
frameworks.
"""

pdf_path = export_pdf(
    sample_report
)

docx_path = export_docx(
    sample_report
)

md_path = export_markdown(
    sample_report
)

print(pdf_path)
print(docx_path)
print(md_path)