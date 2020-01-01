import cv2
import matplotlib.pyplot as plt
# 对图像模糊化

img = cv2.imread(r'./pic/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = [5, 11, 17]
# (1)
# fig, axs = plt.subplots(nrows=1, ncols=3, figsize = (20, 20))
# for index, s in enumerate(kernel):
#     img_blurred = cv2.blur(img, ksize=(s,s))
#     ax = axs[index]
#     ax.imshow(img_blurred)
#     ax.axis('off')
# plt.show()



# (2)
# 平均模糊
img_0 = cv2.blur(img, ksize=(7, 7))
# 高斯模糊
img_1 = cv2.GaussianBlur(img, ksize=(7, 7), sigmaX=0)
# 中值模糊
img_2 = cv2.medianBlur(img, 7)
# 双边滤波
img_3 = cv2.bilateralFilter(img, 7, sigmaSpace=75, sigmaColor=75)
images = [img_0, img_1, img_2, img_3]
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(20, 20))
for i, p in enumerate(images):
    ax = axs[i]
    ax.imshow(p)
    ax.axis('off')
plt.show()