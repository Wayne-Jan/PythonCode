import tensorflow as tf

# 檢查 TensorFlow 是否能夠檢測到 GPU
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    print(f"已偵測到 {len(gpus)} 個 GPU。")
else:
    print("未偵測到 GPU。")

# 顯示 TensorFlow 所使用的設備
for device in tf.config.experimental.list_physical_devices():
    print(device)
