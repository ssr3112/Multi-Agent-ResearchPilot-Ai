from app.graph.state import ResearchState
from app.services.logging_service import add_log


def human_review_agent(
    state: ResearchState
):

    if "approval_status" not in state:

        state["approval_status"] = (
            "pending"
        )

    add_log(
        state,
        "Human Review",
        "Pending Approval"
    )

    return state