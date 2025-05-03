from typing import Any, Dict, List
from openai import AsyncOpenAI
from ..config import get_settings


settings = get_settings()


class BaseAgent:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
            http_client=None
        )
        self.system_prompt = ""
        self.memory: List[Dict[str, Any]] = []

    def set_system_prompt(self, prompt: str) -> None:
        """Set the system prompt for the agent."""
        self.system_prompt = prompt

    def add_to_memory(self, role: str, content: str) -> None:
        """Add a message to the agent's memory."""
        self.memory.append({"role": role, "content": content})

    def clear_memory(self) -> None:
        """Clear the agent's memory."""
        self.memory = []

    async def generate_response(self, user_input: str) -> str:
        """Generate a response based on the user input and agent's memory."""
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add memory messages
        messages.extend(self.memory)
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        # Generate response
        response = await self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=messages
        )
        return response.choices[0].message.content

    def get_memory(self) -> List[Dict[str, Any]]:
        """Get the agent's current memory."""
        return self.memory 