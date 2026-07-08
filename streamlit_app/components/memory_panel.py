import streamlit as st
import requests


def render_memory(api_url):

    st.subheader(
        "🧠 Research Memory"
    )

    memory_query = st.text_input(
        "Search Previous Research"
    )

    if st.button(
        "Search Memory"
    ):

        response = requests.get(
            f"{api_url}/api/memory",
            params={
                "query":
                memory_query
            }
        )

        if response.status_code == 200:

            results = response.json()[
                "results"
            ]

            if results:

                for result in results:

                    with st.expander(
                        "Memory Result"
                    ):

                        st.write(
                            result
                        )

            else:

                st.warning(
                    "No similar research found."
                )