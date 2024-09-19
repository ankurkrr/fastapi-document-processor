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
```

2.Create and activate a virtual environment (recommended):

```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.Install the required dependencies:

```bash
Copy code
pip install -r requirements.txt
```

4.Set up MongoDB:

If using MongoDB Atlas, create a cluster, get the connection string, and replace the MongoDB URI in your FastAPI app configuration.
If using Local MongoDB, ensure MongoDB is running and update the connection string accordingly.

5.Run the FastAPI application:

```bash
Copy code
uvicorn main:app --reload
```
6.Access the API:

Once the application is running, open your browser and go to:

```bash
Copy code
http://127.0.0.1:8000
```
8.API Documentation:

You can explore the interactive API docs at:

```bash
Copy code
http://127.0.0.1:8000/docs
```


# Running with Docker (Optional)


1.Build the Docker image:

```bash
Copy code
docker build -t fastapi-document-processor .
```

2.Run the container:

```bash
Copy code
docker run -d -p 8000:8000 fastapi-document-processor
```
The API will be accessible at http://localhost:8000.

# Using Postman for API Testing

1.Install Postman:

Download and install Postman from https://www.postman.com/downloads/.

2.Create a new request:

Open Postman and create a new HTTP request (GET, POST, etc.).

3.Set the URL:

For local testing, set the URL to http://127.0.0.1:8000.
For example, to test PDF processing, you can set the URL to http://127.0.0.1:8000/process-pdf.

4.Testing with POST requests:
*To test the PDF and URL processing endpoints, choose the POST method and attach files or JSON in the Body tab of Postman:

      - For PDF Processing:
            Select POST.
            URL: http://127.0.0.1:8000/process-pdf.
            In Body, choose form-data and upload a PDF file.

          
      - For URL Processing:
            Select POST.
            URL: http://127.0.0.1:8000/process-url.
            In Body, select raw and input a JSON object like:

            
```json
Copy code
{
  "url": "https://example.com"
}
```

5. View the Response:

Send the request, and you will receive the extracted text, embeddings, or chatbot responses in the Response section of Postman.

