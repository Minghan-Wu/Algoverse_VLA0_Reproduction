#!/bin/bash
# Clone VLA-0 and LIBERO dependencies

echo "Cloning VLA-0 and LIBERO..."

# Clone VLA-0 repo
if [ ! -d "vla0" ]; then
    git clone https://github.com/NVlabs/vla0.git
    echo "✅ VLA-0 cloned"
fi

# Clone LIBERO benchmark
if [ ! -d "vla0/libs/LIBERO" ]; then
    git clone https://github.com/Lifelong-ML/LIBERO.git vla0/libs/LIBERO
    echo "✅ LIBERO cloned"
fi

echo "✅ Dependencies cloned!"
