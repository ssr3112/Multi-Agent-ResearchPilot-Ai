import streamlit as st




def render_export(report):

    from app.tools.exporter import (
    export_pdf,
    export_docx,
    export_markdown
    )

    st.subheader(
        "📥 Export Center"
    )

    if (
        st.session_state.approval_status
        !=
        "approved"
    ):

        st.info(
            "Approve report before exporting."
        )

        return

    pdf_path = export_pdf(
        report
    )

    docx_path = export_docx(
        report
    )

    md_path = export_markdown(
        report
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        with open(
            pdf_path,
            "rb"
        ) as f:

            st.download_button(
                label="📄 PDF",
                data=f,
                file_name="research_report.pdf"
            )

    with c2:

        with open(
            docx_path,
            "rb"
        ) as f:

            st.download_button(
                label="📝 DOCX",
                data=f,
                file_name="research_report.docx"
            )

    with c3:

        with open(
            md_path,
            "rb"
        ) as f:

            st.download_button(
                label="📘 Markdown",
                data=f,
                file_name="research_report.md"
            )