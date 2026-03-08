#!/bin/bash
set -e  # Exit on error

cd /kaggle/working/Algoverse_VLA0_Reproduction

# Core robotics deps
pip install -q "robosuite[rendering]==1.4.0" mujoco==3.1.6 gymnasium

# RoboVerse FULL source install (has evals.libero)
git clone https://github.com/RoboVerseOrg/RoboVerse.git roboverse_source
cd roboverse_source
pip install -e ".[il]"  # Imitation learning (evals.libero)
cd ..

# LIBERO install
cd vla0/libs
pip install -e LIBERO
cd ../..

# VLA-0 + paths
pip install -e vla0
export PYTHONPATH="${PYTHONPATH}:$(pwd)/vla0:$(pwd)/roboverse_source"

echo "✅ VLA-0 + RoboVerse + LIBERO ready!"
python -c "from roboverse.evals.libero.eval import eval; print('✅ roboverse.evals.libero OK!')"

