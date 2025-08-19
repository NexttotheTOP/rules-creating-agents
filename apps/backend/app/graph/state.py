from typing import Any, Dict, List, Optional, TypedDict


class GraphState(TypedDict):
    user_input: str
    project_structure: Optional[List[Dict[str, Any]]]
    rules: Optional[List[Dict[str, Any]]]
    visualization: Optional[str]


class GraphConfig(TypedDict):
    supervisor_agent: Dict[str, Any]
    generator_agent: Dict[str, Any]
    reflexion_agent: Dict[str, Any]
    visualization_agent: Dict[str, Any]
