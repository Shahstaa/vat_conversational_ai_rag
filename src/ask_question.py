from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load the vector database
vector_store = Chroma(persist_directory="data/vector_db", embedding_function=OpenAIEmbeddings())

# Create a Retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vector_store.as_retriever()
)

def ask_question(question):
    return qa_chain.run(question)

# Test the function
if __name__ == "__main__":
    question = "What is the VAT rate in Bahrain?"
    print("Answer:", ask_question(question))
