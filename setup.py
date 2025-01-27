from setuptools import setup, find_packages

setup(
    name="elena",
    version="0.1.0",
    description="Multi-agent AI framework built on DeepSeek",
    author="Elena Team",
    packages=find_packages(),
    install_requires=[
        "deepseek-ai>=0.1.0",
        "pydantic>=2.0.0",
        "python-dotenv>=0.19.0",
        "aiohttp>=3.8.0",
        "asyncio>=3.4.3",
    ],
    python_requires=">=3.8",
)
