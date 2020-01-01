import cv2
import numpy as np
import matplotlib.pyplot as plt
# 形态转换

img = cv2.imread(r'./pic/1.jpg')

'''
# (1)
kernel_0 = np.ones((9, 9), np.uint8)
kernel_1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
kernel_2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (9, 9))
kernels = [kernel_0, kernel_1, kernel_2]

# 腐蚀
# plt.figure(figsize = (20, 20))
# for i in range(3):
#     img_copy = img.copy()
#     img_copy = cv2.erode(img_copy, kernels[i], iterations = 3)
#     plt.subplot(1, 3, i+1)
#     plt.imshow(img_copy)
#     plt.axis('off')
# plt.show()


# (2)扩张
# kernel = np.ones((9, 9), np.uint8)
# img_dilate = cv2.dilate(img, kernel, iterations = 3)
# plt.figure(figsize = (20, 10))
# plt.subplot(1, 2, 1); plt.imshow(img, cmap="gray")
# plt.subplot(1, 2, 2); plt.imshow(img_dilate, cmap="gray")
# plt.show()
'''



# (3)
kernel = np.ones((9, 9), np.uint8)
img_open = cv2.morphologyEx(img, op= cv2.MORPH_OPEN, kernel=kernel)
img_close = cv2.morphologyEx(img, op= cv2.MORPH_CLOSE, kernel=kernel)
img_grad = cv2.morphologyEx(img, op= cv2.MORPH_GRADIENT, kernel=kernel)
img_tophat = cv2.morphologyEx(img, op= cv2.MORPH_TOPHAT, kernel=kernel)
img_blackhat = cv2.morphologyEx(img, op= cv2.MORPH_BLACKHAT, kernel=kernel)
# Plot the images
images = [img, img_open, img_close, img_grad,
          img_tophat, img_blackhat]
fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (15, 15))
for ind, p in enumerate(images):
    ax = axs[ind//3, ind%3]
    ax.imshow(p, cmap = 'gray')
    ax.axis('off')
plt.show()