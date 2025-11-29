from fastapi import APIRouter, Depends
from app.modules.schemas import SummarizeRequestSchema, SummarizeResponse
from app.modules.services.summarizer_service import (
    SummarizerService,
    get_summarizer_service,
)

router = APIRouter(prefix="/summarize", tags=["summarizer"])


@router.post("/", response_model=SummarizeResponse)
async def summarize(
    payload: SummarizeRequestSchema,
    summarize_service: SummarizerService = Depends(get_summarizer_service),
):
    """
    Summarizes user-provided text using SummarizerService.

    Notes:
    - Accepts a plain string as input.
    - Returns a summarized plain string.
    - Delegates the actual summarization logic to the service layer.
    """
    try:
        summary = await summarize_service.generate_summary(payload.text)
        return SummarizeResponse(summary=summary)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
