# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("image/21.jpg", cv2.IMREAD_COLOR)

# 회색조
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

# 반복문을 사용하여 색인값과 하위 윤곽선 정보로 반복한다. 근사치 정확도를 계산하기 위해 윤곽선 전체 길이의 2%로 활용함.
# cv2.arcLength(윤곽선, 폐곡선)
# 윤곽선 : 검출된 윤곽선들이 저장된 Numpy 배열.
# 폐곡선 : 검출된 윤곽선이 닫혀있는지, 열여있는지 설정.
# 다각형 근사는 더글라스-패커(Douglas-Peucker) 알고리즘을 사용함.
# 반복과 끝점을 이용해 선분으로 구성된 윤곽선들을 더 적은 수의 윤곽점으로 동일하거나 비슷한 윤곽선으로 데시메이트(decimate) 함.
for contour in contours:
    epsilon = cv2.arcLength(contour, True) * 0.02
    approx_poly = cv2.approxPolyDP(contour, epsilon, True)

    for approx in approx_poly:
        cv2.circle(src, tuple(approx[0]), 3, (255, 0, 0), -1)

# 이미지 출력 함수
cv2.imshow("src", src)
# 키 입력 대기함수
cv2.waitKey(0)
# 모든 윈도우 창 제거함수
cv2.destroyAllWindows()