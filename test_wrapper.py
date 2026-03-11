#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

print("🚀 Stage 2 VLM Wrapper Test - Control Generation")
print("Status: Testing proprioception + Python function generation")
print("-" * 50)

from src.level_reduction import VLMWrapper

# Initialize wrapper
wrapper = VLMWrapper("qwen2.5-coder")

# Mock robot state (matching the meeting notes: step index + arm position)
task = "pick up the red bowl"
current_arm_position = [0.1, 0.2, 0.5, 0.0, 0.0, 0.0, 1.0]
previous_action = [0.01, 0.0, -0.05, 0.0, 0.0, 0.0, 1.0]

print("\nCalling VLM for next ~5 steps of code...")

# Call the new method you just added
generated_code = wrapper.generate_action_function(
    task=task,
    proprioception=current_arm_position,
    previous_controls=previous_action
)

print("\n✅ GENERATED PYTHON CODE FROM VLM:")
print("-" * 30)
print(generated_code)
print("-" * 30)
print("✅ Test Complete! Ready for Dhia to plug into the simulation loop.")
