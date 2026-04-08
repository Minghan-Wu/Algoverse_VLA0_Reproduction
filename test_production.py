import sys
sys.path.insert(0, '.')

from src.level_reduction import VLMWrapper
from pathlib import Path

# Simulate LIBERO pipeline
wrapper = VLMWrapper("qwen2.5-coder-7b")
image_path = Path("mock_libero_image.jpg")

code = wrapper.process_image(str(image_path))
print("✅ Production: Generated robot code")
print(f"Code length: {len(code)} chars")
