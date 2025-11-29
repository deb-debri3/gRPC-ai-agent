from pydantic import BaseModel


class SummarizeRequestSchema(BaseModel):
    text: str


class SummarizeResponse(BaseModel):
    summary: str
