import cv2
import numpy as np
import matplotlib.pyplot as plt
# 人脸检测

path = r'.\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(path)

def detect_face(img):

    img_copy = img.copy()
    # print(type(img_copy))
    face_rects = face_cascade.detectMultiScale(img_copy)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (255, 255, 255), 3)

    return img_copy

# Step 2. Call the cam
# cap = cv2.VideoCapture(r'.\video\AOA.mp4')
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    # print(ret)
    # cv2.imshow('frame', frame)

    frame = detect_face(frame)
    cv2.imshow('Video Face Detection', frame)


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()