# Import Library
import cv2

# 동영상 파일 설정
cap = cv2.VideoCapture("동영상경로")

# 33초 동안 반복
while cv2.waitKey(33) < 0:
    # 현재 동영상의 프레임 수와 동영상의 총 프레임 수를 받아온다.
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_POS_FRAMES):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)