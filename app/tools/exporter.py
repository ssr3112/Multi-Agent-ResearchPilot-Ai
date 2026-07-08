import os

from docx import Document

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


EXPORT_DIR = "exports"

os.makedirs(
    EXPORT_DIR,
    exist_ok=True
)


def export_markdown(
    report: str,
    filename="research_report.md"
):

    path = os.path.join(
        EXPORT_DIR,
        filename
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    return path


def export_docx(
    report: str,
    filename="research_report.docx"
):

    path = os.path.join(
        EXPORT_DIR,
        filename
    )

    doc = Document()

    doc.add_paragraph(
        report
    )

    doc.save(path)

    return path


def export_pdf(
    report: str,
    filename="research_report.pdf"
):

    path = os.path.join(
        EXPORT_DIR,
        filename
    )

    pdf = SimpleDocTemplate(
        path
    )

    styles = getSampleStyleSheet()

    content = [
        Paragraph(
            report.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    ]

    pdf.build(content)

    return path