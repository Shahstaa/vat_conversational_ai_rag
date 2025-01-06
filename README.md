# VAT Conversational AI
This project implements a Conversational AI Interface using Retrieval-Augmented Generation (RAG) to answer VAT-related questions based on NBR Bahrain's VAT Guide.

## Live Demo

You can access the live version of the app here:

[**VAT Conversational AI - Live Demo**]

## Features
- **Text Extraction**: Extracts text from a PDF VAT Guide document.
- **Data Storage**: Stores the extracted text as embeddings in a vector database using ChromaDB.
- **Conversational Interface**: Users can ask VAT-related questions and receive relevant answers based on the VAT guide.
- **Streamlit Web Interface**: Simple and professional web interface to interact with the AI.

## Tech Stack
- **Python**: The backend programming language used for processing the data and running the AI.
- **OpenAI API**: Powers the conversational AI for question answering.
- **Streamlit**: A framework for building the web interface.
- **ChromaDB**: A vector database used for storing and retrieving VAT-related content.
- **PDFMiner**: Used for extracting text from the VAT Guide PDF.
- **Langchain**: Framework for building the RAG pipeline.

# vat_conversational_ai_rag
