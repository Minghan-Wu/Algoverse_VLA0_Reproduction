import base64
from typing import Optional
from pathlib import Path

def get_system_prompt():
    """Embedded system prompt - no external dependencies."""
    return """You are an expert robotic control Vision-Language Model. 
Your goal is to write short-horizon, executable Python control snippets to achieve a task based on an image observation.

CRITICAL RULES:
1. DO NOT output raw numerical joint action sequences (like [128, 130, 127]).
2. DO NOT output conversational text, explanations, or markdown blocks. Output ONLY valid Python code.
3. You must use a `while` loop for robust generalization (visual servoing).

You have access to the following predefined Robot API functions:
- `get_object_position(object_name: str) -> list[float]` (Returns [x, y, z])
- `get_gripper_position() -> list[float]` (Returns [x, y, z])
- `move_arm_by_delta(dx: float, dy: float, dz: float)`
- `close_gripper()`
- `open_gripper()`
- `is_aligned() -> bool`

EXAMPLE OUTPUT for task "pick up the red bowl":
```python
target = get_object_position("red bowl")
while not is_aligned():
    current_pos = get_gripper_position()
    dx = target - current_pos
    dy = target - current_pos
    move_arm_by_delta(dx, dy, 0)
close_gripper()
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
