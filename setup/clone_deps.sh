#!/bin/bash
# Clone VLA-0 and LIBERO dependencies

echo "Cloning VLA-0 and LIBERO..."

# Clone VLA-0 repo
if [ ! -d "vla0" ]; then
    git clone https://github.com/NVlabs/vla0.git
fi

# Clone LIBERO benchmark
if [ ! -d "vla0/libs/LIBERO" ]; then
    git clone https://github.com/Lifelong-ML/libero-benchmark.git vla0/libs/LIBERO
fi

echo "✅ Dependencies cloned!"
