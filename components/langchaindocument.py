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
    "search",
    "Use ONLY for questions about LangChain documentation, APIs, or tutorials. Do NOT use for creative tasks, greetings, or general writing."
)