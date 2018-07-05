import cv2 as cv
import numpy as np 
from glob import glob
from matplotlib import pyplot as plt 

def histogram_plot(cdf_normalized):
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(), 255, [0, 256], color = 'r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'))
    plt.show()

def histogram_equalisation(img): #name was the second parameter
    ####odredjivanje kumulativne verovatnoce piksela
    hist, bins = np.histogram(img.flatten(), 256, [0, 255])
    cdf_original = hist.cumsum()
    cdf_normalized = cdf_original * hist.max() / cdf_original.max()

    cdf_modified = np.ma.masked_equal(cdf_original, 0) 
    cdf_modified = ((cdf_modified - cdf_modified.min())*255)/(cdf_modified.max()-cdf_modified.min())
    cdf_original = np.ma.filled(cdf_modified, 0).astype('uint8')

    img2 = cdf_original[img]
    # hist_output = np.array(img2.flatten())
    cv.imwrite("greyscaled-pics/first_method/imgmod.jpg", img2)
    # histogram_plot(cdf_normalized)
    #histogram_plot(cdf_modified)

    return img2.flatten()

#za svaku sliku u direktorijumu poziva funkciju hist-equ
# for fn in glob("test_images/*"):
#     print(fn)
#     img = cv.imread(fn, 0)
#     hist, bins = np.histogram(img.flatten(), 256, [0, 255])
#     histogram_equalisation(img, fn.split("/")[-1])

cv.waitKey()