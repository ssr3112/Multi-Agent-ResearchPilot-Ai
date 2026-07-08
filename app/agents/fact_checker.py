from app.graph.state import ResearchState

from app.services.claim_extractor import (
    extract_claims
)

from app.services.confidence_service import (
    calculate_confidence
)

from app.services.logging_service import (
    add_log
)


def fact_checker_agent(
    state: ResearchState
):

    verified_claims = []

    for article in state["extracted_content"]:

        article_claims = []

        for chunk in article["chunks"][:2]:

            claims = extract_claims(chunk)

            article_claims.extend(
                claims
            )

        for claim in article_claims:

            verified_claims.append(
                {
                    "claim": claim,
                    "confidence": calculate_confidence(
                        len(state["sources"])
                    ),
                    "sources": [
                        article["url"]
                    ]
                }
            )

    state["verified_claims"] = (
        verified_claims
    )

    add_log(
        state,
        "Fact Checker Agent",
        "Completed"
    )

    return state