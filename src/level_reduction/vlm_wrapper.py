import base64
from typing import Optional
from pathlib import Path

def get_system_prompt():
    """Embedded system prompt - no external dependencies."""
    return """You are an expert robotic control Vision-Language Model. 
Your goal is to write a short-horizon, executable Python function to achieve a task based on the current state.

CRITICAL RULES:
1. Output ONLY a valid Python function named `generate_control(time_step: int, proprioception: list[float]) -> list[float]`.
2. DO NOT output raw numerical joint action sequences (like [128, 130, 127]) outside the function.
3. DO NOT output conversational text, explanations, or markdown blocks. 
4. The function must return a list of 7 control values [x, y, z, roll, pitch, yaw, gripper].

EXAMPLE OUTPUT for task "pick up the red bowl":
```python
def generate_control(time_step: int, proprioception: list[float]) -> list[float]:
    # Target joint angles based on time_step
    if time_step < 5:
        # Move down towards the bowl
        return [0.0, 0.0, -0.05, 0.0, 0.0, 0.0, 1.0] 
    else:
        # Close gripper
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]
```"""

class VLMWrapper:
    def __init__(self, model_name: str = "qwen2.5-coder"):
        self.model_name = model_name
        self.system_prompt = get_system_prompt()
        print(f"✅ VLMWrapper initialized: {model_name}")

    def process_image(self, image_path: str) -> str:
        """Placeholder for image processing."""
        print(f"Processing image: {image_path}")
        return "mock_image_data"

    def generate_action_function(self, task: str, proprioception: list[float], previous_controls: list = None) -> str:
        """
        Generates a Python function for the next ~5 steps.
        Matches meeting notes: takes proprioception and previous controls as context.
        """
        print(f"Generating control function for task: '{task}'")
        print(f"Context -> Proprioception: {proprioception}")
        if previous_controls:
            print(f"Context -> Previous controls: {previous_controls}")
        
        # In Stage 2, this will call the VLM API. For now, we return mock Python code.
        mock_generated_code = """
        def generate_control(time_step: int, proprioception: list[float]) -> list[float]:
            # Move forward
            return [0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        """
        return mock_generated_code.strip()