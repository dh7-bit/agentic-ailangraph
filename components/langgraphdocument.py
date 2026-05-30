from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import create_retriever_tool
from retreivertool import retriver
langchain_urls=[
"https://docs.langchain.com/oss/python/langgraph/workflows-agents",
    "https://docs.langchain.com/oss/python/langgraph/overview",
    "https://docs.langchain.com/oss/python/langgraph/graph-api#map-reduce-and-the-send-api"
]
docs=[WebBaseLoader(url).load() for url in langchain_urls]
doclist=[item for sublist in docs for item in sublist]
retriever=retriver(doclist)
retriever_tool_langgraph = create_retriever_tool(
    retriever,
    "search",
    "Use ONLY for questions about LangGraph documentation, APIs, or tutorials. Do NOT use for creative tasks, greetings, or general writing."
)