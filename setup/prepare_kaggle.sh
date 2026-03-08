#!/bin/bash
# Run this AFTER downloading the model with download_qwen_model.py
pip install roboverse robosuite==1.4.0 mujoco gymnasium lerobot
echo "✅ Kaggle env ready!

set -e  # Exit on any error

echo "Setting up VLA-0 model folder structure..."

# 1. Create the pytorch_model folder the script expects
mkdir -p /kaggle/working/local_qwen_model/pytorch_model

# 2. Move HF config files into the expected folder
mv /kaggle/working/local_qwen_model/*.json /kaggle/working/local_qwen_model/pytorch_model/ 2>/dev/null || true
mv /kaggle/working/local_qwen_model/*.safetensors /kaggle/working/local_qwen_model/pytorch_model/ 2>/dev/null || true
mv /kaggle/working/local_qwen_model/*.txt /kaggle/working/local_qwen_model/pytorch_model/ 2>/dev/null || true

# 3. Rename .bin to .pth (bypass the assert model_path[-4:] == '.pth')
mv /kaggle/working/local_qwen_model/pytorch_model.bin /kaggle/working/local_qwen_model/pytorch_model.pth 2>/dev/null || true

# 4. Symlink config.yaml where the script expects it
ln -sf /kaggle/working/configs/config.yaml /kaggle/working/local_qwen_model/config.yaml

echo "✅ Setup complete!"
ls -la /kaggle/working/local_qwen_model/
