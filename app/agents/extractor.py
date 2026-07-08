from app.graph.state import ResearchState
from app.services.chunking_service import chunk_text
from app.services.logging_service import add_log


def extractor_agent(
    state: ResearchState
):

    extracted_content = []

    for source in state["sources"]:

        content = source["content"]

        chunks = chunk_text(content)

        extracted_content.append(
            {
                "title": source["title"],
                "url": source["url"],
                "chunks": chunks
            }
        )

    state["extracted_content"] = extracted_content

    add_log(
        state,
        "Extractor Agent",
        "Completed"
    )

    return state