from langchain_openai import ChatOpenAI
from apps.backend.app.graph.state import GraphState
from langchain_core.messages import HumanMessage, SystemMessage
import logging
from apps.backend.app.prompts.PRDanalysis import PRD_ANALYSIS_PROMPT
import os
from dotenv import load_dotenv
from typing import AsyncGenerator, Dict, Any

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ------------------------------------------------------------
# Building Context Info
# ------------------------------------------------------------

def build_context_info(prd_text: str) -> str:   
    """Build context information for the PRD analysis."""
    return 

# ------------------------------------------------------------
# PRD Analysis Agent
# ------------------------------------------------------------

class PRDAnalysisAgent:
    """Agent that analyzes PRD text and extracts key features, tasks, and considerations."""

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",    
            temperature=1, 
            streaming=True
        )
        self.logger = logging.getLogger(__name__)

    async def analyze_prd(
            self, 
            state: GraphState
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """Agent that analyzes PRD text and extracts key features, tasks, and considerations."""
        self.logger.info("Starting PRD analysis")
        prd_text = state["user_input"]
        messages = [
            SystemMessage(content=PRD_ANALYSIS_PROMPT),
            HumanMessage(content=prd_text)
        ]
        async for chunk in self.llm.astream(messages):
            token = chunk.content if hasattr(chunk, "content") else str(chunk)
            yield {"visualization": token}
