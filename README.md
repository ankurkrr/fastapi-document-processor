# FastAPI Document Processor

This project is a FastAPI-based application that processes URLs and PDFs, extracts text, generates sentence embeddings, and stores the data in a MongoDB database. The app also provides a chatbot functionality that allows users to ask questions based on processed documents using semantic search with embeddings.

## Features

- **URL Processing**: Scrapes text content from a given URL.
- **PDF Processing**: Extracts text from uploaded PDF files.
- **Text Embeddings**: Generates sentence embeddings using the `sentence-transformers` library.
- **MongoDB Integration**: Stores content and embeddings in a MongoDB database.
- **Semantic Search**: Implements a simple chatbot that allows users to ask questions about the stored documents based on semantic similarity.

## Tech Stack

- **FastAPI**: Web framework for building the API.
- **MongoDB**: NoSQL database to store documents and embeddings.
- **Sentence Transformers**: Library to generate sentence embeddings for semantic search.
- **BeautifulSoup**: For web scraping of URL content.
- **PyPDF2**: For extracting text from PDF files.

## Installation

### Prerequisites

- **Python 3.10+**
- **MongoDB Atlas or Local MongoDB instance**
- **Docker (optional)**

### Local Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-document-processor.git
cd fastapi-document-processor