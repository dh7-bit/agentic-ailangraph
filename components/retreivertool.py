from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embeddingmodel import embeddings
def retriver(doclist):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    doc_splites=text_splitter.split_documents(doclist)
    vectorstore=FAISS.from_documents(documents=doc_splites,embedding=embeddings)
    retriever=vectorstore.as_retriever()
    return retriever