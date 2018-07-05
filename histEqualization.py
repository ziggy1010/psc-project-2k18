import cv2 as cv; from matplotlib import pyplot as plt; import numpy as np


def imgHist(img):
    img = cv.imread('test_images', cv.IMREAD_GRAYSCALE)
    img2 = img.equalizeHist(img)
    plt.imshow([img2] ,cmap='red')
    cv.imshow(img2)
    plt.show()


img = cv.imread('test_images', cv.IMREAD_GRAYSCALE)
imgHist(img)