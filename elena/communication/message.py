"""
Message handling for Elena framework.
"""
from typing import Dict, Any, List
from datetime import datetime

class Message:
    """
    Message class for agent communication.
    """
    def __init__(
        self,
        sender: str,
        content: str,
        msg_type: str = "text",
        metadata: Dict[str, Any] = None
    ):
        self.sender = sender
        self.content = content
        self.msg_type = msg_type
        self.metadata = metadata or {}
        self.timestamp = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary format."""
        return {
            "sender": self.sender,
            "content": self.content,
            "type": self.msg_type,
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Create message from dictionary format."""
        return cls(
            sender=data["sender"],
            content=data["content"],
            msg_type=data["type"],
            metadata=data["metadata"]
        )
