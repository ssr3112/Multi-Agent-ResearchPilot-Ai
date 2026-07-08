# test_memory_search.py

from app.tools.memory import (
    search_memory
)

results = search_memory(
    "LangGraph"
)

for doc in results:

    print(
        doc.page_content
    )

    print("-" * 50)