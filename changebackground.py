import cv2
import numpy as np
from PIL import Image, ImageDraw

img_path = r'.\pic\picyq.jpg'

img = Image.open(img_path)
w, h = img.size
background = Image.new('RGB', (w, h), (255, 255, 255))
background.save(r'.\pic\back.jpg')
# background.show()

img = cv2.imread(img_path)
back = cv2.imread(r'.\pic\back.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([78, 43, 46])
upper_blue = np.array([110, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

erode = cv2.erode(mask, None, iterations=3)
# cv2.imshow('erode', erode)
dilate = cv2.dilate(erode, None, iterations=3)
# cv2.imshow('dilate', dilate)
pic = cv2.cvtColor(dilate, cv2.COLOR_HSV2BGR)
cv2.imshow('pic', pic)

center = [w / 2, h / 2]
for i in range(h):
    for j in range(w):
        if dilate[i, j] == 0:  # 0代表黑色的点
            back[center[0] + i, center[1] + j] = img[i, j]  # 此处替换颜色，为BGR通道
cv2.imshow('res', back)

# cv2.imshow('img', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()

# img = Image.open(img_path)
# # pixel = img.getpixel((14, 10))
# # print(pixel)
# w, h = img.size
# # print(w, h)
# for row in range(h):
#     for col in range(w):
#         pixel = img.getpixel((col, row))
#         print(pixel)
#         if col == 2:
#             break

# img.show()
