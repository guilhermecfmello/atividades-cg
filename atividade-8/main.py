import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
from Otsu import Otsu

# Arguments tratment function
def getArgs(args, param):
    try:
        argValue = False
        for a in args:
            if(a == '-h'):
                print('============= Help Menu =============')
                print("Exec format: python3 main.py [args] | python main.py -h for help")
                print("\n\nCommands:")
                print('-i "imageName"')
                return False
        for i in range(1, len(args)):
            if(args[i] == param):
                argValue = args[i+1]
        if(argValue == False): raise Exception("Param " + str(param) + " couldn't be found")
        return argValue
    except Exception as e:
        print("Exec format: python main.py [args] | python main.py -h for help.\nError: " + str(e))
        exit()  


if __name__ == '__main__':
    imgName = getArgs(sys.argv, "-i")
    img = cv.imread('images/' + imgName, 0)
    otsu = Otsu(img.shape[0] * img.shape[1])
    hist = otsu.calcHist(img)
    probHist = otsu.calcProb()
    v = 0
    for t in range(1, otsu.lMax - 1):
        probC1, probC2 = otsu.probClass(probHist, t)
        globalAvg, avgC1, avgC2 = otsu.mediaItensity(
            probHist, t, probC1, probC2)
        variance = (probC1*(avgC1 - globalAvg)**2) + \
            (probC2*(avgC2 - globalAvg)**2)
        if variance > v:
            v = variance
            T = t
    r = otsu.applyT(img, T)
    otsu.showImg('', r)
    cv.imwrite('threshold-img.jpg', r)
