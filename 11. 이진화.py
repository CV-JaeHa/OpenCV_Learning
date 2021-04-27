# Import Library
import cv2

# 이진화 : 어느 지점을 기준으로 값이 높거나 낮은 픽셀의 값을 대상으로 특정 연산을 수행할 때 사용.
# 기준값에 따라 이분법적으로 구분해 픽셀을 참 혹은 거짓으로 나눈다.

# 이미지 경로 설정
src = cv2.imread("image/11.jpg", cv2.IMREAD_COLOR)

# 그레이로 설정
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 이진화 함수(cv2.threshold) : 그레일 스케일 이미지에 이진화를 적용 할 수 있다.
# retval, dst = cv2.threshold(src, thresh, maxval, type) : 입력 이미지(src)를 임곗값 형식(type)에 따라 임곗값(thresh)과 최댓값(maxval)을 활용하여 설정 임곗값(retval)과 결과 이미지(dst)를 반환함.
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# 이미지 출력 함수
cv2.imshow("dst", dst)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 제거 함수
cv2.destroyAllWindows()