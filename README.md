# Algoverse VLA‑0 Reproduction

## How to run on Kaggle

1. **Clone this repo**
   ```bash
   !git clone https://github.com/Minghan‑Wu/Algoverse_VLA0_Reproduction.git
   %cd Algoverse_VLA0_Reproduction

2. **Install dependencies**
   ```bash
   !pip install -r requirements.txt

3. **Download the model**
   ```bash
   !python scripts/download_qwen_model.py

4. **Prepare the model folder structure**
   ```bash
   !bash setup/prepare_kaggle.sh

5. **Run evaluation**
   ```bash
   !python scripts/run_eval_safely.py

