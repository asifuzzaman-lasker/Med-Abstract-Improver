from pydantic import BaseModel

class AbstractRequest(BaseModel):
    abstract: str
    style: str
