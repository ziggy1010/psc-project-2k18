import cv2 as cv; from glob import glob; from matplotlib import pyplot as plt
import numpy as np

#img = cv.imread('test_images/majin_kanon/IMG_5141.JPG', 0)

def imgHist(img):
    hist = np.histogram(img.flatten(), 256, [0, 256])
    hist = plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('histogram'))
    plt.show()   

def clahe(img): #name was the second parameter
    clahe = cv.createCLAHE(clipLimit = 2.0, tileGridSize = (16, 16))
    cli = clahe.apply(img) 
    cv.imwrite("greyscaled-pics/second-method/imgmod2.jpg", cli)
    return cli.flatten()
    # imgHist(img)
    # imgHist(cli)

# for fn in glob("test_images/*"):
#     print(fn)
#     img = cv.imread(fn, 0)
#     clahe(img, fn.split("/")[-1])