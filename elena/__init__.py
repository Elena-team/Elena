"""
Elena - Multi-agent AI framework built on DeepSeek
"""
from .agents.base import BaseAgent
from .agents.group import AgentGroup
from .core.model import DeepSeekModel
from .core.deepseek_integration import DeepSeekIntegration, ModelConfig
from .communication.message import Message
from .task_management.orchestrator import TaskOrchestrator
from .tools.registry import ToolRegistry

__version__ = "0.1.0"

__all__ = [
    "BaseAgent",
    "AgentGroup",
    "DeepSeekModel",
    "DeepSeekIntegration",
    "ModelConfig",
    "Message",
    "TaskOrchestrator",
    "ToolRegistry",
]
