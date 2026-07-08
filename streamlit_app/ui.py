import sys
import os

ROOT_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if ROOT_DIR not in sys.path:
    sys.path.insert(
        0,
        ROOT_DIR
    )



import streamlit as st
import requests

from components.dashboard import render_dashboard
from components.report_view import render_report
from components.review_panel import render_review
from components.export_panel import render_export
from components.memory_panel import render_memory

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="ResearchPilot AI",
    page_icon="🔍",
    layout="wide"
)

# ------------------
# Session State
# ------------------

defaults = {
    "report": "",
    "logs": [],
    "approval_status": "pending",
    "sources_count": 0,
    "claims_count": 0,
    "review_time": ""
}

for k, v in defaults.items():

    if k not in st.session_state:

        st.session_state[k] = v

# ------------------
# Styling
# ------------------

st.markdown("""
<style>

.block-container{
padding-top:1rem;
max-width:1200px;
}

.stButton button{
width:100%;
height:50px;
border-radius:12px;
font-weight:600;
}

</style>
""",
unsafe_allow_html=True)

# ------------------
# Sidebar
# ------------------

with st.sidebar:

    st.title(
        "🔍 ResearchPilot AI"
    )

    st.markdown("---")

    st.caption(
        "LangGraph + Groq + Tavily + FAISS"
    )

# ------------------
# Header
# ------------------

st.title(
    "🔍 ResearchPilot AI"
)

st.caption(
    "Multi-Agent Research & Report Assistant"
)

# ------------------
# Dashboard
# ------------------

render_dashboard(
    st.session_state.sources_count,
    st.session_state.claims_count,
    st.session_state.approval_status
)

# ------------------
# Query
# ------------------

query = st.text_area(
    "Research Query",
    height=120,
    placeholder=
    "Example: Latest AI Agent Frameworks in 2026"
)

if st.button(
    "🚀 Generate Research Report"
):

    if query.strip():

        with st.spinner(
            "Running Multi-Agent Workflow..."
        ):

            response = requests.post(
                f"{API_URL}/api/research",
                json={
                    "query":
                    query
                }
            )
            print("Status:", response.status_code)
            print("Response:", response.text)

        if (
            response.status_code
            ==
            200
        ):

            data = response.json()

            st.session_state.report = (
                data["report"]
            )

            st.session_state.logs = (
                data["logs"]
            )

            st.session_state.approval_status = (
                data["approval_status"]
            )

            st.session_state.sources_count = (
                data["sources_count"]
            )

            st.session_state.claims_count = (
                data["claims_count"]
            )

            st.rerun()

# ------------------
# Report Section
# ------------------

if st.session_state.report:

    render_report(
        st.session_state.report
    )

    st.markdown("---")

    render_review(
        API_URL
    )

    st.markdown("---")

    render_export(
        st.session_state.report
    )

    st.markdown("---")

    with st.expander(
        "📜 Agent Timeline"
    ):

        for log in (
            st.session_state.logs
        ):

            st.success(
                log["agent"]
            )

    st.markdown("---")

    render_memory(
        API_URL
    )