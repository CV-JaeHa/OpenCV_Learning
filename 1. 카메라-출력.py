# 카메라 출력

# Import Library
import cv2

# 웹 캠 출력함수
# 0번은 내장 카메라 1번부터 순서대로 외장 카메라
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)

# waitKey() 키 안의 지정된 시간동안 실행
# 계속 실행시킬때
# while cap.isOpened():
while cv2.waitKey(33) < 0:
    # read() 카메라의 상태와 프레임을 받아온다.
    # ret은 카메라의 상태를 받아오면 정상 : True / 비정상 : False 반환
    # Frame은 현재 시점의 프레임을 저장함.
    ret, frame = cap.read()
    # imshow(윈도우이름, 이미지) : 윈도우 창의 제목(win name)과 이미지(mat)
    cv2.imshow("VideoFrame", frame)

# 메모리 해제
cap.release()
# 모든 윈도우창 제거 함수
cv2.destroyAllWindows()
# 특정 윈도우만 닫기
# cv2.desktoryWindow(윈도우창이름)
