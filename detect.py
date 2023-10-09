import cv2
from cvzone.PoseModule import PoseDetector


cap = cv2.VideoCapture(r'data\Footwork_Tutorial___Dance_Tutorial___chamkela_chehra___Badshah(360p).mp4')
detector = PoseDetector()

pose_lst = []
while cap.isOpened():
    ret , frame = cap.read()
    img = detector.findPose(img=frame)
    landmarks , bboxInfo = detector.findPosition(img=img)

    if bboxInfo:
    # print(bboxInfo)
        landmarks_string = ''
        for lm in landmarks:
            landmarks_string += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
        pose_lst.append(landmarks_string)
        print(len(landmarks_string))
            # print(img.shape[0])

    with open('points.txt','w') as f:
        f.writelines(["%s\n" % item for item in pose_lst])

    cv2.imshow('window',img)
    # print(landmarks)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv2.destroyAllWindows()



