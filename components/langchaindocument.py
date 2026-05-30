from langchain_community.document_loaders import WebBaseLoader
from retreivertool import retriver
from langchain_core.tools.retriever import create_retriever_tool
urls = [
    "https://python.langchain.com/docs/tutorials/",
"https://python.langchain.com/docs/tutorials/chatbot/",
"https://python.langchain.com/docs/tutorials/qa_chat_history/"
]
docs=[]
for url in urls:
    docss=WebBaseLoader([url]).load()
    docs.append(docss)

doclist=[item for sublist in docs for item in sublist]
retriever=retriver(doclist)
retriever_tool_langchain = create_retriever_tool(
    retriever,
    "langchain_search",
 """
    Search the LangChain knowledge base.

    MUST use this tool for any question about:
    - LangChain
    - ToolNode
    - APIs
    - Documentation
    - Tutorials

    Always search before answering these topics.
    Do not answer from prior knowledge.
    """
)