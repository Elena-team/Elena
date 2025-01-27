"""
Agent group coordination and management.
"""
from typing import List, Dict, Any, Optional
from .base import BaseAgent
from ..communication.message import Message
from ..task_management.orchestrator import TaskOrchestrator

class AgentGroup:
    """
    Manages a group of agents working together on tasks.
    Coordinates communication and task distribution.
    """
    def __init__(self, agents: List[BaseAgent]):
        self.agents = {agent.name: agent for agent in agents}
        self.orchestrator = TaskOrchestrator()
        self._initialize_agents()

    def _initialize_agents(self):
        """Register agents with the orchestrator."""
        for agent in self.agents.values():
            self.orchestrator.register_agent(agent)

    async def broadcast_message(self, message: Message):
        """Send message to all agents in the group."""
        responses = {}
        for agent in self.agents.values():
            response = await agent.process_message(message.to_dict())
            responses[agent.name] = response
        return responses

    async def execute_task(
        self,
        task: str,
        task_config: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute a task using the agent group.
        Automatically distributes subtasks and manages coordination.
        """
        task_spec = {
            "description": task,
            "config": task_config or {},
            "agents": list(self.agents.keys())
        }
        
        # Create and execute task
        task_id = await self.orchestrator.create_task(task_spec)
        result = await self.orchestrator.execute_task(task_id)
        return result

    def add_agent(self, agent: BaseAgent):
        """Add a new agent to the group."""
        self.agents[agent.name] = agent
        self.orchestrator.register_agent(agent)

    def remove_agent(self, agent_name: str):
        """Remove an agent from the group."""
        if agent_name in self.agents:
            del self.agents[agent_name]
