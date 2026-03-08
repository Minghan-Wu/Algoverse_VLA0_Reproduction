#!/bin/bash

# Kaggle VLA-0 FULL environment
cd /kaggle/working/Algoverse_VLA0_Reproduction

# Core deps
pip install -q robosuite==1.4.0 mujoco gymnasium torch torchvision transformers

# Clone + install RoboVerse (has evals.libero)
git clone https://github.com/RoboVerseOrg/RoboVerse.git roboverse_full
pip install -e ./roboverse_full

# Clone + install LIBERO
cd vla0/libs
pip install -e LIBERO

# VLA-0 paths
export PYTHONPATH="${PYTHONPATH}:$(pwd)/../vla0:$(pwd)/../vla0/libs/LIBERO"

echo "✅ FULL VLA-0 environment ready!"
