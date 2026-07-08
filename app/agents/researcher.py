from app.tools.web_search import search_web
from app.services.logging_service import add_log
from app.graph.state import ResearchState


def researcher_agent(state: ResearchState):

    query = state["query"]

    results = search_web(query)

    sources = []

    for result in results:

        sources.append(
            {
                "title": result["title"],
                "url": result["url"],
                "content": result["content"]
            }
        )

    state["sources"] = sources

    add_log(
        state,
        "Researcher Agent",
        "Completed"
    )

    return state