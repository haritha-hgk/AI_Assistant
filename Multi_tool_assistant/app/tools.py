from langchain_core.tools import tool
from app.rag import retrieve_docs
from duckduckgo_search import DDGS

@tool
def pdf_search(query: str) -> str:
    """Search company PDF documents"""
    return retrieve_docs(query)

@tool
def calculator(expression: str) -> str:
    """Solve math expressions"""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

@tool
def web_search(query: str) -> str:
    """Search the web"""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)

    return "\n".join(
        f"{r['title']} - {r['body']}" for r in results
    )