# Import Library
import cv2

# 역상(Reverse Image)는 영상이나 이미지를 반전된 색상으로 변환하기 위해 사용.

# 이미지 경로 지정
src = cv2.imread("image/10.jpg", cv2.IMREAD_COLOR)
# src2 = cv2.imread("image/11.jpg", cv2.IMREAD_COLOR)
# NOT 연산 함수
# cv2.bitwise_not(src, mask) : 입력이미지(src), 마스크(mask)로 출력 이미지(dst)를 생성함.
# ps. "not" 연산 이외에도 "and", "or", "xor" 연산이 존재한다.
dst = cv2.bitwise_not(src)
# dst = cv2.bitwise_or(src, src2)

# 이미지 출력 함수
cv2.imshow("src", src)
# cv2.imshow("src2", src2)
cv2.imshow("dst", dst)
# 키 입력 대기 함수
cv2.waitKey()
# 모든 윈도우 창 삭제 함수
cv2.destroyAllWindows()