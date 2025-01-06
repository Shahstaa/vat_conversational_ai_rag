from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Read the cleaned text
with open("data/cleaned_vat_text.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Split text into smaller sections
sections = data.split(". ")  # Split by sentences for simplicity
# Create embeddings and vector database
embeddings = OpenAIEmbeddings()
vector_store = Chroma.from_texts(sections, embeddings)
vector_store.persist()

print("Vector database created and saved to '/vector_db'")