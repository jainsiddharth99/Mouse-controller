import cv2
import numpy as np

import pyautogui


pyautogui.FAILSAFE = False
SCREEN_X, SCREEN_Y = pyautogui.size()
CLICK = CLICK_MESSAGE = MOVEMENT_START = None


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    CAMERA_X, CAMERA_Y, channels = img.shape

    img = cv2.flip(img, 1)
    crop_img = img
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    cv2.imshow('video', grey)
    max_area = -1




    k = cv2.waitKey(10)
    if k == 27:
        break
video_capture.release()
cv2.destroyAllWindows()
