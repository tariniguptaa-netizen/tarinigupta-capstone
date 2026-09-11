from pydantic import BaseModel,Field

class Question(BaseModel):

    question: str = Field(..., min_length=1)


class Answer(BaseModel):
    content: str
    cost_usd: float = 0.0001
    retries: int = 0
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    sources: list[str] = Field(default_factory=list)
    schema_version: str = "v1"