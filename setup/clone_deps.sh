#!/bin/bash
# Clone VLA-0 and LIBERO dependencies

echo "Cloning VLA-0 and LIBERO... (~2 minutes)"

# Clone VLA-0 (timeout 60s)
timeout 60 git clone https://github.com/NVlabs/vla0.git || {
    echo "⚠️ VLA-0 clone failed (timeout), skipping..."
}

# Clone LIBERO (public repo, timeout 60s)
timeout 60 git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git vla0/libs/LIBERO || {
    echo "⚠️ LIBERO clone failed (timeout), skipping..."
}

echo "✅ Dependencies setup complete"
ls -la vla0/ 2>/dev/null || echo "No vla0 folder (skipped due to timeout)"
