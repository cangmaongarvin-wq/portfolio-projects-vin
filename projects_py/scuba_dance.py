import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
scuba_video = cv2.VideoCapture('vids_/cat_scuba.mp4')
detector = HandDetector(detectionCon = 0.8, maxHands = 1)

is_playing = False

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType = False, draw=False)

    if hands:
        hand = hands[0]
        if hand["type"] == "Right":
            is_playing = True

    else:
        is_playing = False
        scuba_video.set(cv2.CAP_PROP_POS_FRAMES, 0)

        if cv2.getWindowProperty("SCUBAAA CAT DANCE", cv2.WND_PROP_VISIBLE) >=1:
            cv2.destroyWindow("SCUBAAA CAT DANCE")
    
    if is_playing:
        success_v, frame_v = scuba_video.read()
        if success_v:
            frame_v = cv2.resize(frame_v, (500, 500))
            cv2.imshow("SCUBAAA CAT DANCE", frame_v)
        else:
            scuba_video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cv2.imshow("Main Feed", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()