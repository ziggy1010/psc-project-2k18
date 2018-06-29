import cv2 as cv; from glob import glob
import numpy as np

#img = cv.imread('test_images/majin_kanon/IMG_5141.JPG', 0)

def clahe(img, name):
    clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
    cli = clahe.apply(img)
    cv.imwrite("greyscaled-pics/second-method/" + name, cli)

for fn in glob("test_images/majin_kanon/*"):
    print(fn)
    img = cv.imread(fn, 0)
    clahe(img, fn.split("/")[-1])
#cv.imwrite('kurac2.jpg', cli)