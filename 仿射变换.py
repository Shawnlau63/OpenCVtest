import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r'pic/4.jpg')
# cv2.imshow('img', img)
# cv2.waitKey(0)

'''缩放'''
# w, h = img.shape[:2]
# 不同缩放插值方法1
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_BITS)
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_BITS2)
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LANCZOS4)
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR_EXACT)
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
# res = cv2.resize(img, (2 * w, 2 * h), interpolation=cv2.INTER_CUBIC)

# cv2.imshow('res', res)
# cv2.waitKey(0)


'''平移'''
# rows, cols = img.shape[:2]
#
# M = np.float32([[1, 0, 100], [0, 1, 50]])
# dst = cv2.warpAffine(img, M, (cols, rows))
#
# cv2.imshow('img', img)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''旋转'''
# rows, cols = img.shape[:2]
#
# # cols-1 and rows-1 are the coordinate limits.
# M = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 45, 1)
# dst = cv2.warpAffine(img, M, (cols, rows))
#
# cv2.imshow('img', img)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''仿射变换'''
# rows, cols, ch = img.shape
#
# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
#
# M = cv2.getAffineTransform(pts1, pts2)
#
# dst = cv2.warpAffine(img, M, (cols, rows))
#
# plt.subplot(121), plt.imshow(img), plt.title('Input')
# plt.subplot(122), plt.imshow(dst), plt.title('Output')
# plt.show()


'''透视变换'''
rows, cols, ch = img.shape

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
