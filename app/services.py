import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import pdfplumber
from io import BytesIO


embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def scrape_url_content(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.get_text(separator=' ')
    return content.strip()

def extract_pdf_text(file: bytes) -> str:
    with pdfplumber.open(BytesIO(file)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return " ".join(text.split())

def generate_embeddings(text: str):
    return embedding_model.encode(text)


import numpy as np


def search_content(query_embedding, document_embeddings, document_content):
    similarity_scores = np.dot(document_embeddings, query_embedding) / (
            np.linalg.norm(document_embeddings) * np.linalg.norm(query_embedding)
    )
    most_similar_index = np.argmax(similarity_scores)

    if isinstance(document_content, bytes):
        document_content = document_content.decode('utf-8')

    sentences = document_content.split('. ')
    return sentences[most_similar_index] if most_similar_index < len(sentences) else "No relevant content found."

