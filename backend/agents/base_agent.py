from typing import Dict, Any
import autogen

class BaseAgent:
    def __init__(self, name: str, system_message: str):
        self.name = name
        self.agent = autogen.AssistantAgent(
            name=name,
            system_message=system_message,
            llm_config={
                "config_list": [{"model": "gpt-4", "api_key": "YOUR_API_KEY"}],
                "temperature": 0.7,
            }
        )
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the input data and return the result
        To be implemented by child classes
        """
        raise NotImplementedError("Child classes must implement this method") 