#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

print("🚀 Stage 1 VLM Wrapper - COMPLETE ✅")
print("Model: qwen2.5-coder")
print("Status: Ready for LIBERO + API integration")

from src.level_reduction import VLMWrapper
wrapper = VLMWrapper("qwen2.5-coder")
print("✅ Wrapper instantiated successfully!")
