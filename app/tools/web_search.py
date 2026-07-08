from tavily import TavilyClient

from app.config.settings import settings

tavily_client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


def search_web(query: str):

    response = tavily_client.search(
        query=query,
        max_results=settings.MAX_SEARCH_RESULTS
    )

    return response.get("results", [])