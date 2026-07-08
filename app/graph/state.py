from typing import TypedDict


class ResearchState(TypedDict):

    query: str

    sources: list

    extracted_content: list

    verified_claims: list

    report: str

    approval_status: str

    logs: list