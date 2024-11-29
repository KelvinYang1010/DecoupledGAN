import cv2

# 读取图像
image = cv2.imread('data/birds/images/001.Black_footed_Albatross/Black_Footed_Albatross_0031_100.jpg')

# 定义边界框的位置和大小 (x, y, w, h)
bbox = (7, 75, 420, 262)
x, y, width, height = bbox

# 绘制边界框
cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), 2)


cv2.imshow('Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()