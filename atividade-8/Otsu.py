import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

LMAX = 256


class Otsu:
    
    def __init__(self, totalPixel):
        self.totalPix = totalPixel
        self.lMax = LMAX
    
    def calcHist(self, img):
        h, w = img.shape
        hist = np.zeros((LMAX))
        for i in range(h):
            for j in range(w):
                hist[img[i, j]] += 1
        self.hist = hist
        return hist


    def calcProb(self):
        prob = np.zeros((LMAX))
        for i in range(self.hist.size):
            prob[i] = self.hist[i]/self.totalPix
        return prob


    def probClass(self, hist, T):
        c1 = c2 = 0
        for i in range(T):
            c1 += hist[i]
        c2 = 1 - c1
        return (c1, c2)


    def mediaItensity(self, hist, T, pc1, pc2):
        s1 = s2 = 0
        for i in range(T):
            s1 += i*hist[i]
        m1 = s1/pc1
        for i in range(T, LMAX):
            s2 += i*hist[i]
        m2 = s2/pc2
        mg = s1 + s2
        return (mg, m1, m2)


    def showHist(self, hist):
        plt.xlim([-0.5, 255.5])
        plt.plot(hist)
        plt.show()


    def applyT(self, img, T):
        result = np.zeros(img.shape)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if(img[i, j] <= T):
                    result[i, j] = 0
                elif(img[i, j] > T):
                    result[i, j] = 255
        return result


    def showImg(self, title, img):
        cv.imshow(title, img)
        k = cv.waitKey(0) & 0xFF
        if k == 27 or k == ord('q'):
            cv.destroyAllWindows()