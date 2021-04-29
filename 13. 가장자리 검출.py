# Import Library
import cv2

# 이미지 출력 함수
src = cv2.imread("image/13.jpg", cv2.IMREAD_COLOR)
# 이미지 회색 계열로 바꾸기
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 이미지 가장자리 검출 함수
# cv2.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)
# : 입력 이미지(src)에 출력 이미지 정밀도(ddepth)를 설정하고 dx(X 방향 미분 차수), dy(Y 방향 미분 함수), 커널크기(ksize), 비율(scale), 오프셋(delta), 테두리 외삽법(borderType)을 설정하여 결과 이미지(dst)를 반환.
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
# 라플라시안 함수 : 입력 이미지에서 가장자리를 검출 할 수 있다.
# cv2.laplacian(src, ddepth, ksie, scale, delta, borderType)
# : 입력이미지(src)에 출력 이미지 정밀도(ddepth)를 설정하고 커널 크기(ksize), 비율(scale), 오프셋(delta), 테두리 외삼법(borderType)을 설정하여 결과 이미지(dst) 반환.
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
# 캐니 함수 : 입력 이미지에서 가장자리를 검출 할 수 있다.
# cv2.Canny(src, threshold1, threshold2, apertureSize, L2gradient)
# : 입력 이미지(src)를 하위 임곗값(threshold1), 상위 임계값(threshold2), 소벨 연산자 마스크 크기(apertureSize), L2 그레이디언트(L2gradient)을 설정해서 결과 이미지(dst) 반환.
canny = cv2.Canny(src, 100, 255)

# 이미지 출력 함수
cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()