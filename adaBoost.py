import cv2 as cv; import numpy as np; from glob import glob
from clahe import * 
from histEqualisation import * 
from linNormalization import * 
import sys 

clahe_adaboost = lambda x: clahe(x, "kurcic")
he_adaboost = lambda x: histogram_equalisation(x, "kurcic2")
ln_adaboost = lambda x: linNormalization(x, "kurcic3")

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

def f(x, w1, w2, w3, f1, f2, f3):
    return w1*f1(x) + w2*f2(x) + w3*f3(x)

def calcError(weight1, weight2, weight3, f1, f2, f3): #error function
    epsilon = 0
    for i in range(img_num):
        epsilon += ((mama(img.flatten(), weight1, weight2, weight3, f1, f2, f3) - wanted_output1)**2)
    return epsilon / img_num

def linCombination(img, f1, f2, f3): #linear combination of methods
    l = sys.argv[1] - sys.argv[0]
    min_error = 10**9
    res = (None, None, None)
    for weight1 in frange(sys.argv[0], sys.argv[1], 0.1):
        sys.stdout.write("%f%%\r" % 100*(eight1 - sys.argv[0]) / l)
        for weight2 in frange(0, 10, 0.1):
            for weight3 in frange(0, 10, 0.1):
                #lin_combination = weight1*img.flatten()+weight2*img.flatten()+weight3*img.flatten()
                error = calcError(weight1, weight2, weight3, f1, f2, f3) 
                if error < min_error: 
                    min_error = error
                    print(min_error)
                    res = (weight1, weight2, weight3)
    print("Weights for this process: %f %f %f" % res)


for fn in glob("greyscaled-pics/first_method/all_pics/*"):
    img = cv.imread(fn, 0)
    img_arr = img.flatten()
    linCombination(img_arr, clahe_adaboost, he_adaboost, ln_adaboost)
