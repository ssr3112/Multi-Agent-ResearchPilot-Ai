import streamlit as st


def render_dashboard(
    sources_count,
    claims_count,
    approval_status
):

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "📚 Sources",
            sources_count
        )

    with c2:
        st.metric(
            "📝 Claims",
            claims_count
        )

    with c3:
        st.metric(
            "✅ Status",
            approval_status
        )