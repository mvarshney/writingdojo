from typing import Any, Dict, List
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from config import get_settings

settings = get_settings()

class BaseAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name=settings.OPENAI_MODEL,
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
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
        messages = [
            SystemMessage(content=self.system_prompt)
        ]
        
        # Add memory messages
        for message in self.memory:
            if message["role"] == "user":
                messages.append(HumanMessage(content=message["content"]))
            else:
                messages.append(SystemMessage(content=message["content"]))
        
        # Add current user input
        messages.append(HumanMessage(content=user_input))
        
        # Generate response
        response = await self.llm.agenerate([messages])
        return response.generations[0][0].text

    def get_memory(self) -> List[Dict[str, Any]]:
        """Get the agent's current memory."""
        return self.memory 