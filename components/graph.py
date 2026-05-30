from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import MessagesState
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import tools_condition,ToolNode
from functions import agent, route_after_agent, norag, grade_documents, generate, rewrite
from toollist import tools
graph=StateGraph(MessagesState)
# memory=MemorySaver()
graph.add_node('agent',agent)
graph.add_node('tools',ToolNode(tools))
graph.add_node('no_tool',norag)
graph.add_node('generate',generate)
graph.add_node('rewrite',rewrite)
graph.add_edge(START,'agent')
graph.add_conditional_edges(
    "agent",
    route_after_agent,
    {
        "tools": "tools",
        "no_tool":'no_tool'
    }
)
graph.add_edge('no_tool',END)
graph.add_conditional_edges('tools',grade_documents,{
    'generate':'generate',
    'rewrite':'rewrite'
})
graph.add_edge('rewrite','agent')
graph.add_edge('generate',END)
builder=graph.compile()