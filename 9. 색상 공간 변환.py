# Import Library
import cv2

# 이미지 경로 설정
src = cv2.imread("이미지 경로", cv2.IMREAD_COLOR)
# 이미지 색상 공간 변경
# cv2.cvtColor(src, code, dstCn) : 입력 이미지(src), 색상변환코드(code), 출력채널(dstCn)으로 출력이미지(dst)를 생성합니다.
# 색상 변환 코드는 원본 이미지, 색상 공간 결과 이미지 색상 공간을 의미합니다.
# 원본 이미지 색상 공간은 원본 이미지와 일치해야 합니다.
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 이미지 출력 함수
cv2.imshow("src", src)
cv2.imshow("dst", dst)
# 키 입력 대기 함수
cv2.waitKey()
# 윈도우 창 제거 함수
cv2.destroyAllWindows()