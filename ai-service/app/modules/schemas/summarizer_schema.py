from pydantic import BaseModel


class SummarizerRequestSchema(BaseModel):
    line: int
    text: str


class SummarizerResponseSchema(BaseModel):
    summary: str
