import cv2 as cv 
import numpy as np

img = cv.imread('test_images/majin_kanon/IMG_5141.JPG', 0)

clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
cli = clahe.apply(img)
cv.imwrite('kurac2.jpg', cli)