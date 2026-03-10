from pydantic import BaseModel

class Prompt_send(BaseModel):
    question: str


class LLMOut(BaseModel):
    answer: str