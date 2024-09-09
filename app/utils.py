import requests
from bs4 import BeautifulSoup
import pdfplumber

def scrape_url_content(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.get_text(strip=True)

def extract_pdf_text(file) -> str:
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return " ".join(text.split())

def clean_content(content: str) -> str:
    return content.strip()
