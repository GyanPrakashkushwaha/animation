import cv2
from cvzone.PoseModule import PoseDetector


cap = cv2.VideoCapture(r'data\Footwork_Tutorial___Dance_Tutorial___chamkela_chehra___Badshah(360p).mp4')
detector = PoseDetector()
while cap.isOpened():
    ret , frame = cap.read()
    img = detector.findPose(img=frame)
    landmarks , bboxInfo = detector.findPosition(img=img)

    cv2.imshow('window',img)
    print(landmarks)

    if cv2.waitKey(10) & 0xFF == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()


