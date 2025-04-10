import cv2
import mediapipe as mp

# 加载视频文件
cap = cv2.VideoCapture('./video/hh.mp4')

# 创建MediaPipe Pose Estimation实例
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 将帧转换为RGB格式
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 运行MediaPipe Pose Estimation
    results = pose.process(rgb_frame)

    # 提取骨骼数据
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            x, y, z = landmark.x, landmark.y, landmark.z
            cv2.circle(frame, (int(x * frame.shape[1]), int(y * frame.shape[0])), 2, (0, 255, 0), -1)

    # 显示视频帧
    cv2.imshow('Video', frame)
    cv2.waitKey(1)