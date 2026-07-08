from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="ResearchPilot AI",
    version="1.0.0"
)

app.include_router(
    router,
    prefix="/api",
    tags=["Research"]
)


@app.get("/")
def health():

    return {
        "status": "running",
        "project": "ResearchPilot AI"
    }