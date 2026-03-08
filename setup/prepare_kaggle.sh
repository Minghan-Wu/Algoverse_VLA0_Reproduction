#!/bin/bash

# Kaggle VLA-0 environment setup
pip install -q roboverse robosuite==1.4.0 mujoco gymnasium lerobot torch torchvision transformers

# Add vla0 to Python path
echo "export PYTHONPATH=\$PYTHONPATH:$(pwd)/vla0" >> ~/.bashrc
source ~/.bashrc

# LIBERO path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/vla0/libs/LIBERO"

echo "✅ Kaggle environment ready!"
echo "PYTHONPATH: $PYTHONPATH"
