from typing import Literal
from langchain_core.prompts import PromptTemplate
from groq import BaseModel
from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model
import os
from langchain_core.messages import AIMessage, SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition
from langchain.chat_models import init_chat_model
from unstructured_client import Field
from langchain_core.prompts import ChatPromptTemplate
from toollist import tools
def agent(state:MessagesState):
    """Invokes the agent model to generate a response based on the current state. Given the question, it will decide to retrieve using the retriever tool, or simply end.
Args:
state (messages):
The current state
Returns:
dict: The updated state with the agent response appended to messages"""
    llm=init_chat_model("llama-3.3-70b-versatile",model_provider="groq",api_key=os.getenv('GROQ'))
    bindllm=llm.bind_tools(tools)
    res=bindllm.invoke(state['messages'])
    return {"messages":[res]}
def route_after_agent(state):
    last_msg = state["messages"][-1]

    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        return "tools"
    else:
        return "no_tool"

def norag(state:MessagesState):
    """normal no tool answer"""
    return {
        "messages": [
            AIMessage(
                content="I can only answer questions related to the knowledge base."
            )
        ]
    }

def grade_documents (state) -> Literal ["generates", "rewrite"]:
    """
    Determines whether the retrieved documents are relevant to the question.
    Args: 
    state (messages): The current state
    Returns:
    str: A decision for whether the documents are relevant or not"""
    print("---CHECK RELEVANCE---")
#Data model
    class grades(BaseModel):
      """Binary score for relevance check."""
      binary_score: str =Field(description="Relevance score 'yes' or 'no'")
    model=init_chat_model("llama-3.3-70b-versatile",model_provider="groq",api_key=os.getenv('GROQ'))
    modelwithstructure=model.with_structured_output(grades)
    message=state['messages']
    prompt = PromptTemplate(
        template="""
You are a grader assessing whether a retrieved document is relevant
to a user question.

Retrieved document:
{context}

User question:
{question}

If the document contains information that helps answer the question,
or is semantically related, return:

- yes = relevant
- no = not relevant

Return only the binary score.
""",
        input_variables=["context", "question"],
    )

    chain = prompt | modelwithstructure

    messages = state["messages"]

    human_messages = [
    msg for msg in messages
    if isinstance(msg, HumanMessage)
]
    question = human_messages[-1].content
    print(question)
    docs = messages[-1].content

    scored_result = chain.invoke(
        {
            "question": question,
            "context": docs,
        }
    )

    score = scored_result.binary_score.lower()

    if score == "yes":
        print("---DECISION: DOCS RELEVANT---")
        return "generate"

    print("---DECISION: DOCS NOT RELEVANT---")
    return "rewrite"

def generate(state):
    """
Generate answer
    Args:
        state (messages): The current state
    Returns:
        dict: The updated message
    """
    print("---GENERATE---")
    messages = state["messages"]
    human_messages = [
    msg for msg in messages
    if isinstance(msg, HumanMessage)
]
    question = human_messages[-1].content
    last_message = messages[-1]
    docs = last_message.content
    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the provided context.

Context:
{context}

Question:
{question}

Answer:
""")
    models=init_chat_model("llama-3.3-70b-versatile",model_provider="groq",api_key=os.getenv('GROQ'))
# Post-processing
    def format_docs(docs):
      return "\n\n".join(doc.page_content for doc in docs)
# Chain
    rag_chain=prompt|models

# Run
    response = rag_chain.invoke({"context": docs, "question": question})
    return {"messages": [response]}


def rewrite(state):
    """
    Rewrite the user's question to improve retrieval.
    """

    print("---TRANSFORM QUERY---")
    messages=state['messages']
    human_messages = [
    msg for msg in messages
    if isinstance(msg, HumanMessage)
]
    question = human_messages[-1].content

    model = init_chat_model(
        "llama-3.3-70b-versatile",
        model_provider="groq",
        api_key=os.getenv("GROQ")
    )

    response = model.invoke(
        [
            HumanMessage(
                content=f"""
You are a query rewriter for a RAG system.

Analyze the user's question and rewrite it to be more specific,
clear, and retrieval-friendly while preserving the original intent.

Original question:
{question}

Improved question:
"""
            )
        ]
    )

    return {"messages": [response]}
