from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

# Load PDF
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

# Split text into chunks
def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)

# Create vector database
def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    return db

# Ask question
def ask_question(db, query):
    docs = db.similarity_search(query, k=3)  # only top 3 chunks

    context = "\n\n".join([doc.page_content for doc in docs])

    from langchain_ollama import OllamaLLM
    llm = OllamaLLM(model="tinyllama")

    prompt = f"""
You are an AI assistant.

Answer ONLY from the given context.
If answer is not clearly present, say: "Not found in document".

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response