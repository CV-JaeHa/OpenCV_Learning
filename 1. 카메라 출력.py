# Import Library
import cv2

# 노트북 웹캠 설정
# 0은 내장 캠이고 외장캠을 사용할 경우에는ㄴ 1~n까지 차례로 채워짐
cap = cv2.VideoCapture(0)

# cap.set(propid, value)로 카메라의 propid(속성)와, value(값)을 설정 할 수 있다.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)

while cv2.waitKey(33) < 0: # wait 키 안의 지정된 시간동안
    # read()는 카메라의 상태와 프레임을 받아옵니다.
    # ret은 카메라의 상태를 받아오면 정상이면 True 아니면 False를 반환합니다.
    # Frame은 현재 시점의 프레임을 저장합니다.
    ret, frame = cap.read()
    # imshow(윈도우이름, 이미지) : 윈도우 창의 제목(winname)과 이미지(mat)
    cv2.imshow("VideoFrame", frame)

# 메모리 해제
cap.release()
# 모든 윈도우창 제거 함수
cv2.destroyAllWindows()
# 특정 윈도우만 닫기
# cv2.destoryWindow(윈도우창이름)