import cv2 as cv; import numpy as np; from glob import glob

wanted_output1 = np.array([1, 0, 0, 0, 0]) #majin kanon
wanted_output2 = np.array([0, 1, 0, 0, 0]) #nikolin kanon
wanted_output3 = np.array([0, 0, 1, 0, 0]) #praktica
wanted_output3 = np.array([0, 0, 0, 1, 0]) #samsung
wanted_output4 = np.array([0, 0, 0, 0, 1]) #toki_kanon
img_num = 89

def frange(start, stop, step): #float in for loop
    x = start 
    while x < stop:
        yield x
        x += step

min_error = 99999
def calcError(weight1, weight2, weight3): #error function
    for i in range(img_num):
        epsilon = ((linCombination(img) - wanted_output1)**2)/img_num
        return epsilon

def linCombination(img): #linear combination of methods
    for weight1 in frange(0, 10, 0.1):
        for weight2 in frange(0, 10, 0.1):
            for weight3 in frange(0, 10, 0.1):
                #lin_combination = weight1*img.flatten()+weight2*img.flatten()+weight3*img.flatten()
                error = calcError(weight1, weight2, weight3) 
                if error < min_error: min_error = error; print(min_error)


for fn in glob("greyscaled-pics/first_method/all_pics/*"):
    img = cv.imread(fn, 0)
    img_arr = img.flatten()
    linCombination(img_arr)
