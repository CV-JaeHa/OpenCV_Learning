# Import Library
import cv2

# 로컬 파일을 읽어온다.
src = cv2.imread("이미지경로", cv2.IMREAD_COLOR)

# 해당 이미지의 높이, 너비, 채널의 값을 저장한다.
height, width, channel = src.shape
# 높이와 너비를 이용하여 회전 중심점을 설정한다.
# 회전 변환 행렬을 계산한다.
# 중심점, 각도, 비율, 매핑 변환 행렬 생성
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
# 회전 변환 계산
# 원본이미지에 아핀 맵 행렬을 적용하고 출력이미지 크기로 변형해서 출력이미지를 반
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()