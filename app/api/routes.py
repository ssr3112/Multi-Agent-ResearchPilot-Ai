from fastapi import APIRouter

from app.api.schemas import ResearchRequest
from app.graph.workflow import research_graph
from app.tools.memory import search_memory

router = APIRouter()

review_store = {
    "status": "pending"
}


@router.post("/research")
def generate_research(
    request: ResearchRequest
):

    state = {
        "query": request.query,
        "logs": []
    }

    result = research_graph.invoke(
        state
    )

    return {
        "report": result.get(
            "report",
            ""
        ),

        "logs": result.get(
            "logs",
            []
        ),

        "approval_status": result.get(
            "approval_status",
            "pending"
        ),

        "sources_count": len(
            result.get(
                "sources",
                []
            )
        ),

        "claims_count": len(
            result.get(
                "verified_claims",
                []
            )
        )
    }


@router.get("/memory")
def get_memory(
    query: str
):

    docs = search_memory(
        query
    )

    return {
        "results": [
            doc.page_content
            for doc in docs
        ]
    }


@router.post("/review")
def review_report(
    action: str
):

    review_store["status"] = action

    return {
        "status": action
    }


@router.get("/review")
def get_review_status():

    return review_store