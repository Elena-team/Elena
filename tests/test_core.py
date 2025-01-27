"""
Tests for Elena framework core functionality.
"""
import pytest
from elena import (
    DeepSeekModel,
    ModelConfig,
    DeepSeekIntegration
)

@pytest.mark.asyncio
async def test_model_initialization():
    config = ModelConfig(
        model_name="deepseek-v3",
        temperature=0.7
    )
    model = DeepSeekModel(config.dict())
    await model._initialize_model()
    assert model.integration is not None

@pytest.mark.asyncio
async def test_model_generation():
    model = DeepSeekModel()
    response = await model.generate("Hello, world!")
    assert isinstance(response, str)
    assert len(response) > 0

@pytest.mark.asyncio
async def test_deepseek_integration():
    integration = DeepSeekIntegration()
    await integration.initialize()
    stats = integration.get_token_stats()
    assert "total_tokens" in stats
    assert "active_parameters" in stats
