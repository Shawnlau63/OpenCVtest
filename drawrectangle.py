import cv2
# 绘制矩形操作

drawing = False
ix = -1
iy = -1

def drawRectangle(event, x, y, flags, param):
    # 定义全局变量
    global ix, iy, drawing
    # 按下鼠标左键，则打开绘图，并记录坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        # 若鼠标一等，则绘制相应矩形
        if drawing == True:
            cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1)

    elif event == cv2.EVENT_LBUTTONUP:
        # 若松开鼠标左键则停止绘图
        drawing = False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1)

# 打开图片
img = cv2.imread(r'./pic/0.jpg')

# 给窗口命名
cv2.namedWindow(winname='my drawing')
# 建立窗口与方法内操作的交互连接
cv2.setMouseCallback('my drawing', drawRectangle)

while True:
    cv2.imshow('my drawing', img)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()