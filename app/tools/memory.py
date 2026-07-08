import os

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


MEMORY_PATH = "memory_store/faiss_index"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def save_report(report: str):

    docs = [
        Document(
            page_content=report
        )
    ]

    faiss_file = os.path.join(
        MEMORY_PATH,
        "index.faiss"
    )

    if os.path.exists(faiss_file):

        db = FAISS.load_local(
            MEMORY_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        db.add_documents(
            docs
        )

    else:

        os.makedirs(
            MEMORY_PATH,
            exist_ok=True
        )

        db = FAISS.from_documents(
            docs,
            embeddings
        )

    db.save_local(
        MEMORY_PATH
    )


def search_memory(
    query: str,
    k: int = 3
):

    faiss_file = os.path.join(
        MEMORY_PATH,
        "index.faiss"
    )

    if not os.path.exists(
        faiss_file
    ):
        return []

    db = FAISS.load_local(
        MEMORY_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    results = db.similarity_search(
        query=query,
        k=k
    )

    return results