from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    MAX_SEARCH_RESULTS = int(
        os.getenv("MAX_SEARCH_RESULTS", 5)
    )

settings = Settings()