from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from app.tools import (
    pdf_search,
    calculator,
    web_search
)

# Local LLM
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

# Tools
tools = [
    pdf_search,
    calculator,
    web_search
]

# Memory
memory = MemorySaver()

# Agent
agent = create_react_agent(
    llm,
    tools,
    checkpointer=memory
)