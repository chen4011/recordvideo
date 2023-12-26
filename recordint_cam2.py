import cv2
import threading
import time
from datetime import datetime
import os

# 控制fps的變數
# desired_fps = 30

# 創建以當前日期和時間命名的資料夾
current_datetime = datetime.now().strftime('%Y%m%d_%H%M')
output_directory = os.path.join(
    r"D:\exp_pose2sim\pose2sim\Pose2Sim\Empty_project\cal",
    f"{current_datetime}_int2"
)
os.makedirs(output_directory, exist_ok=True)

# 影片檔案名稱
output_file_cam2 = os.path.join(output_directory, 'int_cam2.mp4')
# output_file_cam2 = os.path.join(output_directory, 'int_cam2.mp4')

# 初始化兩個VideoCapture物件，代表兩台webcam
# cam2 = cv2.VideoCapture(0)  # 修改為第一台webcam的索引
cam2 = cv2.VideoCapture(1)  # 修改為第二台webcam的索引

# 先讀取一帧以加速初始化過程
ret, frame = cam2.read()

# 取得影片的寬、高、FPS等資訊
width = int(cam2.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam2.get(cv2.CAP_PROP_FPS))

# 建立VideoWriter物件，用於寫入錄影檔案
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4編碼器
out_cam2 = cv2.VideoWriter(output_file_cam2, fourcc, fps, (width, height))
# out_cam2 = cv2.VideoWriter(output_file_cam2, fourcc, fps, (width, height))

# 建立Flag，用於控制錄影的開始和停止
recording = False
exit_program = False  # 新增一個用於退出程式的Flag

# 定義一個函式，用於錄影
def record():
    global recording
    while True:
        if recording:
            ret_cam2, frame_cam2 = cam2.read()
            # ret_cam2, frame_cam2 = cam2.read()

            if ret_cam2:
                out_cam2.write(frame_cam2)
                # out_cam2.write(frame_cam2)

                # 即時顯示捕捉到的影像
                cv2.imshow('Camera 1', frame_cam2)
                # cv2.imshow('Camera 2', frame_cam2)

        # 按 'q' 鍵退出即時顯示和錄影
        key = cv2.waitKey(1)
        if key == ord('q') or exit_program:
            break

    # 關閉所有窗口
    cv2.destroyAllWindows()

# 主程式
record_thread = threading.Thread(target=record)
record_thread.daemon = True  # 設置為 daemon
record_thread.start()

while not exit_program:
    command = input("Enter 'b' to begin recording, 'e' to end, or 'q' to quit: ")
    
    if command.lower() == 'b':
        recording = True
        print("Recording started.")
    elif command.lower() == 'e':
        recording = False
        print("Recording stopped.")
    elif command.lower() == 'q':
        exit_program = True  # 修改這裡
        print("Exiting program.")

# 不再使用 record_thread.join()
# 主執行緒終止之前等待片刻
time.sleep(2)

# 釋放資源
cam2.release()
# cam2.release()
out_cam2.release()
# out_cam2.release()