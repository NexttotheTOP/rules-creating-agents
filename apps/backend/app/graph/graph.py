from dotenv import load_dotenv
import os

from langgraph.graph import END, StateGraph
from langchain_core.messages import HumanMessage, AIMessage
from apps.backend.app.graph.state import GraphState
from apps.backend.app.agents import PRDAnalysisAgent
import asyncio

load_dotenv()

# ------------------------------------------------------------
# Graph Setup
# ------------------------------------------------------------

workflow = StateGraph(GraphState)

workflow.add_node("prd_analysis", PRDAnalysisAgent().analyze_prd)

workflow.set_entry_point("prd_analysis")
workflow.add_edge("prd_analysis", END)

app = workflow.compile()

if __name__ == "__main__":
    asyncio.run(
        app.ainvoke(
            {
                "user_input": "I want to build a web app that allows users to create and manage their own projects."
            }
        )
    )
