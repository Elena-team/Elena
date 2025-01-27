"""
Tool registry for Elena framework.
"""
from typing import Dict, Any, Callable

class ToolRegistry:
    """
    Registry for managing and accessing tools.
    """
    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def register_tool(self, name: str, tool_func: Callable):
        """Register a new tool."""
        self.tools[name] = tool_func

    def get_tool(self, name: str) -> Callable:
        """Get a tool by name."""
        return self.tools.get(name)

    def list_tools(self) -> Dict[str, str]:
        """List all available tools."""
        return {name: func.__doc__ for name, func in self.tools.items()}
