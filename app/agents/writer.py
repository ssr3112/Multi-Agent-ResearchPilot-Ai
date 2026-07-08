from app.graph.state import ResearchState
from app.services.llm_service import llm
from app.services.logging_service import add_log
from app.tools.memory import save_report

def writer_agent(state: ResearchState):

    claims_text = "\n".join(
        [
            f"- {claim['claim']}"
            for claim in state["verified_claims"]
        ]
    )

    prompt = f"""
    You are a professional research analyst.

    Create a structured research report using the findings below.

    Format:

    # Executive Summary

    # Key Findings

    # Confidence Analysis

    # References

    Findings:
    {claims_text}

    Write professionally.
    """

    response = llm.invoke(prompt)

    state["report"] = response.content

    save_report(state["report"])

    add_log(
        state,
        "Writer Agent",
        "Completed"
    )

    return state
