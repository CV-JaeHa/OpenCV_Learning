# Import Library
import cv2

# 채널 분리(Split)과 병합(Merge)은 영상이나 이미지의 색상 공간의 채널을 분리하거나 합치기 위해 사용한다.
# ps. OpenCV의 가산 혼합의 삼원 색 기본 배열순서는 BGR이다.

# 이미지 경로 설정
src = cv2.imread("image/16.jpg", cv2.IMREAD_COLOR)
# 채널 분리 함수
# cv2.split(src) : 입력 이미지(src)에서 채널을 분리해 단일 채널 이미지 배열(mv)을 생성함.
# mv는 목록(list) 형식으로 반환되며, b, g, r 등의 형태로 각 목록의 원솟값을 변수로 지정할 수 있음.
b, g, r = cv2.split(src)
# 채널 병합 함수(cv2.merge)로 채널된 채널을 병합해 하나의 이미지로 합칠 수 있다.
# cv2.merge(mv)로 단일 채널 이미지 배열(mv)를 병합해 출력 이미지(dst)를 생성합니다.
inverse = cv2.merge((r, g, b))

# 이미지 출력 함수
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inverse)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()