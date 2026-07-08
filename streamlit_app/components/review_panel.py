import streamlit as st
import requests
from datetime import datetime


def render_review(api_url):

    st.subheader(
        "👨‍💼 Human Review"
    )

    status = st.session_state.approval_status

    if status == "pending":

        st.warning(
            "⏳ Awaiting Human Review"
        )

    elif status == "approved":

        st.success(
            "✅ Human Approved"
        )

    elif status == "revision_requested":

        st.error(
            "🔄 Revision Requested"
        )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "✅ Approve Report"
        ):

            response = requests.post(
                f"{api_url}/api/review",
                params={
                    "action":
                    "approved"
                }
            )

            if response.status_code == 200:

                st.session_state.approval_status = (
                    "approved"
                )

                st.session_state.review_time = (
                    datetime.now().strftime(
                        "%d-%m-%Y %H:%M"
                    )
                )

                st.rerun()

    with c2:

        if st.button(
            "🔄 Request Revision"
        ):

            response = requests.post(
                f"{api_url}/api/review",
                params={
                    "action":
                    "revision_requested"
                }
            )

            if response.status_code == 200:

                st.session_state.approval_status = (
                    "revision_requested"
                )

                st.session_state.review_time = (
                    datetime.now().strftime(
                        "%d-%m-%Y %H:%M"
                    )
                )

                st.rerun()

    if st.session_state.review_time:

        st.caption(
            f"Reviewed at: {st.session_state.review_time}"
        )