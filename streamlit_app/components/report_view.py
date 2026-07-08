import streamlit as st


def render_report(report):

    st.subheader(
        "📄 Research Report"
    )

    st.markdown(
        report
    )