from fastapi import FastAPI
from app.modules.routers.summarizer_router import router as summarizer_router

app = FastAPI(title="AI Agent Service")
app.include_router(summarizer_router)


@app.get("/health")
def health():
    return {"status": "ok"}
