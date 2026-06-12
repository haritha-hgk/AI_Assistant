from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

DB_PATH = "chroma_db"

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

def retrieve_docs(query: str):
    docs = retriever.invoke(query)
    return "\n\n".join([d.page_content for d in docs])