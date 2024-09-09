from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from app.services import scrape_url_content, extract_pdf_text, generate_embeddings, search_content
import uuid
import numpy as np

app = FastAPI()

client = AsyncIOMotorClient("mongodb+srv://fastapi:scrap123@apiservices.lqbvv.mongodb.net/?retryWrites=true&w=majority&appName=apiservices")
db = client['mydb']
collection = db['documents']


class URLRequest(BaseModel):
    url: str


class ChatRequest(BaseModel):
    chat_id: str
    question: str


@app.post("/process_url")
async def process_url(request: URLRequest):
    content = scrape_url_content(request.url)
    chat_id = str(uuid.uuid4())
    embeddings = generate_embeddings(content)
    embeddings_list = embeddings.tolist()

    document = {"chat_id": chat_id, "content": content, "embeddings": embeddings_list}
    await collection.insert_one(document)

    return {"chat_id": chat_id, "message": "URL content processed and stored successfully."}


@app.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text_content = extract_pdf_text(content)
    chat_id = str(uuid.uuid4())
    embeddings = generate_embeddings(text_content)
    embeddings_list = embeddings.tolist()

    document = {"chat_id": chat_id, "content": text_content, "embeddings": embeddings_list}
    await collection.insert_one(document)
    return {"chat_id": chat_id, "message": "PDF content processed and stored successfully."}


@app.post("/chat")
async def chat(request: ChatRequest):
    document = await collection.find_one({"chat_id": request.chat_id})
    if not document:
        return {"response": "No document found for this chat ID."}

    query_embedding = generate_embeddings(request.question)
    stored_embeddings = np.array(document['embeddings'])

    response = search_content(query_embedding, stored_embeddings, document['content'])

    return {"response": response}