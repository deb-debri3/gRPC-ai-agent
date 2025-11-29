from fastapi import APIRouter, Depends
from ..schemas import SummarizerRequestSchema, SummarizerResponseSchema
from ..services import SummarizerServices, get_summarizer_service

router = APIRouter(prefix="/summarizer", tags=["summarizer"])


@router.post("/", response_model=SummarizerResponseSchema)
async def summarize_content(
    payload: SummarizerRequestSchema,
    summarizer_service: SummarizerServices = Depends(get_summarizer_service),
):
    """
    router to summarize user-provided text
    """
    summary = await summarizer_service.generate_summary(payload=payload)
    return SummarizerResponseSchema(summary=summary)
