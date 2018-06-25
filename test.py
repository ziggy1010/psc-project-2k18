import cv2 as cv
import numpy as np 
from glob import glob
from matplotlib import pyplot as plt 


# img = cv.imread("test_images/majin_kanon/IMG_5141.JPG", 0)
# hist, bins = np.histogram(img.flatten(), 256, [0, 256])


def histogram_plot(cdf):
    plt.plot(cdf, color = 'b')
    plt.hist(img.flatten(), 256, [0, 256], color = 'r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'))
    plt.show()

def histogram_equalisation(img, name):
    ####odredjivanje kumulativne verovatnoce piksela
    cdf_original = hist.cumsum()
    cdf_modified = cdf_original * hist.max() / cdf_original.max()

    cdf_modified2 = np.ma.masked_equal(cdf_original, 0)
    cdf_modified2 = (cdf_modified2 - cdf_modified2.min())*255/(cdf_modified2.max()-cdf_modified2.min())
    cdf_original = np.ma.filled(cdf_modified2, 0).astype('uint8')
    ######

    img2 = cdf_original[img]
    hist2 = cv.calcHist([img2],[0],None,[256],[0,256])
    print(name)
    cv.imwrite("greyscaled-pics/" + name, img2)

    #cv.imshow("original", img)
    #cv.imshow("modified", img2)

    histogram_plot(cdf_modified)
    #histogram_plot(hist2)
 

for fn in glob("test_images/majin_kanon/*"):
    print(fn)
    img = cv.imread(fn, 0)
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    histogram_equalisation(img, fn.split("/")[-1])


# histogram_equalisation(img)
cv.waitKey()


