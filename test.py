import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 

img = cv.imread("test_images/majin_kanon/IMG_5156.JPG", 0)
cv.imwrite('greyscaled-pics/original_greyscale.jpg', img)
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

####odredjivanje kumulativne verovatnoce piksela
cdf_original = hist.cumsum()
cdf_modified = cdf_original * hist.max() / cdf_original.max()
###


######
cdf_modified2 = np.ma.masked_equal(cdf_original, 0)
cdf_modified2 = (cdf_modified2 - cdf_modified2.min())*255/(cdf_modified2.max()-cdf_modified2.min())
cdf_original = np.ma.filled(cdf_modified2, 0).astype('uint8')
######


#first picture graph
plt.plot(cdf_modified, color = 'b')
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'))
plt.show()

#modified picture graph
plt.plot(cdf_modified2, color = 'b')
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0, 256])
plt.legend(('cdf2', 'histogram'))
plt.show()

img2 = cdf_original[img]
cv.imshow("modified", img2)
cv.imshow("original", img)
cv.namedWindow('original', cv.WINDOW_NORMAL)
cv.namedWindow('modified', cv.WINDOW_NORMAL)

cv.imwrite("greyscaled-pics/modified.jpg", img2)
cv.waitKey()
