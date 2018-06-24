import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 

img = cv.imread("test.jpg")

hist, bins = np.histogram(img.flatten(), 512, [0, 512])

cdf_original = hist.cumsum()
cdf_modified = cdf_original * hist.max() / cdf_original.max()

plt.plot(cdf_modified, color = 'b')
plt.hist(img.flatten(), 512, [0, 512], color = 'r')
plt.xlim([0, 512])
plt.legend(('cdf', 'histogram'))
plt.show()


cdf_modified2 = np.ma.masked_equal(cdf_original, 0)
cdf_modifed2 = (cdf_modified2 - cdf_modified2.min())*255/(cdf_modified2.max()-cdf_modified2.min())
cdf_original = np.ma.filled(cdf_modified2, 0).astype('uint8')

img2 = cdf_original[img]

cv.imshow("modified", img2)
cv.imshow("original", img)
cv.waitKey()