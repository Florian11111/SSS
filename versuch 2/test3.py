import numpy as np
import cv2
from skimage.color import rgb2gray

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    grayscale = rgb2gray(frame)
    cv2.imshow("test", frame)

cap.release()
cv2.destroyAllWindows()