"""
Basic usage example of the Elena framework.
"""
import asyncio
from elena import (
    BaseAgent,
    AgentGroup,
    DeepSeekModel,
    ModelConfig,
    Message
)

async def main():
    # Configure model
    config = ModelConfig(
        model_name="deepseek-v3",
        temperature=0.7,
        max_tokens=1024
    )

    # Create agents
    assistant = BaseAgent(
        name="assistant",
        role="assistant",
        model_config=config.dict()
    )
    researcher = BaseAgent(
        name="researcher",
        role="researcher",
        model_config=config.dict()
    )

    # Create agent group
    group = AgentGroup([assistant, researcher])

    # Execute task
    result = await group.execute_task(
        "Research and summarize the latest developments in quantum computing"
    )
    print("Task Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
