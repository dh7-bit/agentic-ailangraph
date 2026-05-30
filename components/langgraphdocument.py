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
    "langgraph_search",
 """
    Search the LangGraph knowledge base.

    MUST use this tool for any question about:
    - LangGraph
    - ToolNode
    - APIs
    - Documentation
    - Tutorials

    Always search before answering these topics.
    Do not answer from prior knowledge.
    """)