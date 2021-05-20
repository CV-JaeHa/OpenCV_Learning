# Import Library
import numpy as np
import cv2

# 이미지 경로 설정
# 원본 이미지(src)와 연산 값(number1, number2)를 선언함.
# 연산 이미지는 회색 이미지(127, 127, 127)와 검은색 이미지(2, 2, 2)를 사용함.
src = cv2.imread("image/29.jpg")
number1 = np.ones_like(src) * 127
number2 = np.ones_like(src) * 2

# 더하기
add = cv2.add(src, number1)
# 빼기
sub = cv2.subtract(src, number1)
# 곱하기
mul = cv2.multiply(src, number2)
# 나누기
div = cv2.divide(src, number2)

# 연결 함수(np.concatenate)로 이미지들을 연결함.
src = np.concatenate((src, src, src, src), axis = 1)
number = np.concatenate((number1, number1, number2, number2), axis = 1)
dst = np.concatenate((add, sub, mul, div), axis = 0)

# 이미지 출력 함수
cv2.imshow("dst", dst)
# 키 입력 대기함수
cv2.waitKey(0)
# 모든 윈도우 창 닫기 함수
cv2.destroyAllWindows()