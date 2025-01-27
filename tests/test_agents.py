"""
Tests for Elena framework agent functionality.
"""
import pytest
from elena import BaseAgent, AgentGroup, Message

@pytest.mark.asyncio
async def test_agent_creation():
    agent = BaseAgent(
        name="test_agent",
        role="assistant"
    )
    assert agent.name == "test_agent"
    assert agent.role == "assistant"

@pytest.mark.asyncio
async def test_agent_group():
    agent1 = BaseAgent("agent1", "assistant")
    agent2 = BaseAgent("agent2", "researcher")
    group = AgentGroup([agent1, agent2])
    
    assert len(group.agents) == 2
    assert "agent1" in group.agents
    assert "agent2" in group.agents

@pytest.mark.asyncio
async def test_message_handling():
    agent = BaseAgent("test_agent", "assistant")
    message = Message(
        sender="user",
        content="Hello",
        msg_type="text"
    )
    response = await agent.process_message(message.to_dict())
    assert response is not None
