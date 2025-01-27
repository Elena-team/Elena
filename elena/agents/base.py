"""
Base agent implementation for Elena framework.
"""
from typing import Dict, Any, List, Optional
from ..core.model import DeepSeekModel

class BaseAgent:
    """
    Base class for all Elena agents.
    """
    def __init__(
        self,
        name: str,
        role: str,
        model_config: Optional[Dict[str, Any]] = None
    ):
        self.name = name
        self.role = role
        self.model = DeepSeekModel(model_config)
        self.memory = []
        self.tools = {}

    async def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming message and generate response."""
        # TODO: Implement message processing logic
        pass

    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a given task."""
        # TODO: Implement task execution logic
        pass

    def add_tool(self, tool_name: str, tool_func: callable):
        """Add a tool to the agent's toolkit."""
        self.tools[tool_name] = tool_func
