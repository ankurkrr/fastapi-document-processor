from pydantic import BaseModel

class Document(BaseModel):
    chat_id: str
    content: str
    embeddings: list
