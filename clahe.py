import cv2 as cv; from glob import glob; from matplotlib import pyplot as plt
import numpy as np

#img = cv.imread('test_images/majin_kanon/IMG_5141.JPG', 0)

dir_in = input()
dir_out = input()

def imgHist(img):
    hist = plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('histogram'))
    # plt.show()   

def clahe(img, name):
    clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
    cli = clahe.apply(img)
    cv.imwrite("greyscaled-pics/second-method/" + dir_out + "/"+ name, cli)
    imgHist(img)
    imgHist(cli)

for fn in glob("test_images/"+ dir_in +"/*"):
    print(fn)
    img = cv.imread(fn, 0)
    clahe(img, fn.split("/")[-1])
#cv.imwrite('kurac2.jpg', cli)