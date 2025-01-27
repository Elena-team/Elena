"""
Core DeepSeek model integration for Elena framework.
"""
from typing import Dict, Any, Optional
from .deepseek_integration import DeepSeekIntegration, ModelConfig

class DeepSeekModel:
    """
    Wrapper for DeepSeek model integration.
    Provides high-level interface for model operations.
    """
    def __init__(self, model_config: Optional[Dict[str, Any]] = None):
        config = ModelConfig(**(model_config or {}))
        self.integration = DeepSeekIntegration(config)
        self._initialize_model()

    async def _initialize_model(self):
        """Initialize the DeepSeek model with configuration."""
        await self.integration.initialize()

    async def generate(self, prompt: str, **kwargs) -> str:
        """Generate response using DeepSeek model."""
        return await self.integration.generate(prompt, **kwargs)

    def update_config(self, new_config: Dict[str, Any]):
        """Update model configuration."""
        config = ModelConfig(**new_config)
        self.integration = DeepSeekIntegration(config)
        asyncio.create_task(self._initialize_model())
