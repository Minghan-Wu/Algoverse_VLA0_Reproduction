import os
import sys
import subprocess

# Use default Python (no conda dependency)
python_cmd = ["python"]

libero_path = "/kaggle/working/vla0/libs/LIBERO"
if libero_path not in sys.path:
    sys.path.insert(0, libero_path)
os.environ["PYTHONPATH"] = f"{libero_path}:{os.environ.get('PYTHONPATH', '')}"

subprocess.run([
    *python_cmd,
    "vla0/eval/eval_libero.py",
    "--model_path", "/kaggle/working/local_qwen_model/pytorch_model.pth",  
    "--task_suite_name", "libero_goal",
    "--task_name", "put_the_wine_bottle_on_top_of_the_cabinet"
], input="N\n", text=True)
