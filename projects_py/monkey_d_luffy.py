import cv2
import mediapipe as mp
import numpy as np

# 1. Initialize MediaPipe Pose
mp_pose = mp.solutions.pose #type: ignore
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils #type: ignore

# 2. Open Webcam (Using DirectShow for Windows stability)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# How much to stretch? (2.0 = double length, 3.0 = triple)
STRETCH_FACTOR = 2.5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Empty frame or camera busy.")
        break

    h, w, _ = frame.shape
    # MediaPipe needs RGB, but OpenCV uses BGR
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:
        # Landmarks: Right Shoulder=12, Right Wrist=16
        lm = results.pose_landmarks.landmark
        
        # Get Pixel Coordinates
        shoulder = np.array([lm[12].x * w, lm[12].y * h])
        wrist = np.array([lm[16].x * w, lm[16].y * h])

        # MATH: Calculate the stretch vector
        # (Wrist - Shoulder) = direction and original length
        arm_vector = wrist - shoulder
        gomu_point = shoulder + (arm_vector * STRETCH_FACTOR)

        # DRAW: The "Rubber" Arm (Green line from shoulder to stretched point)
        cv2.line(frame, tuple(shoulder.astype(int)), tuple(gomu_point.astype(int)), (0, 255, 0), 10)
        
        cv2.circle(frame, tuple(gomu_point.astype(int)), 20, (0, 0, 255), -1)

    cv2.imshow('Luffy Gomu Gomu Project', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()