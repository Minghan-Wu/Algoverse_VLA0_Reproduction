from huggingface_hub import snapshot_download

print("Downloading official Qwen2.5-VL-3B-Instruct...")
snapshot_download(
    repo_id="Qwen/Qwen2.5-VL-3B-Instruct",
    local_dir="/kaggle/working/local_qwen_model",
    revision="main"
)
