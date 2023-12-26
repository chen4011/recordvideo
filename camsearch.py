# import cv2

# # for i in range(4):  # 嘗試前 4 個索引
# #     cap = cv2.VideoCapture(i)
# #     if cap.isOpened():
# #         print(f"Webcam {i} is available.")
# #         cap.release()
# cam1 = cv2.VideoCapture(0)
import threading
import time

def daemon_function():
    while True:
        print("Daemon thread is running...")
        print(".")
        time.sleep(1)

# 創建一個daemon執行緒
daemon_thread = threading.Thread(target=daemon_function)
daemon_thread.daemon = True  # 設置為daemon執行緒
daemon_thread.start()

# 主執行緒執行其他工作
for i in range(5):
    print(f"Main thread is working... ({i + 1})")
    time.sleep(2)

print("Main thread is done.")