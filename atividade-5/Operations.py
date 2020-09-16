import numpy as np
import cv2 as cv

class Operations:
    def __init__(self, img):
        self.img = img

    def lowPass(self, img, radius):
        r = np.zeros((img.shape))
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if np.sqrt(i**2+j**2) > radius:
                    r[i, j] = 0
                else:
                    r[i, j] = img[i, j]
        return r


    def highPass(self, img, radius):
        r = np.zeros((img.shape))
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if np.sqrt(i**2+j**2) <= radius:
                    r[i, j] = 0
                else:
                    r[i, j] = img[i, j]
        return r


    def dct(self):
        c = np.zeros((self.img.shape))
        for u in range(c.shape[0]):
            print('Calculudando dct linha ' + str(u))
            for v in range(c.shape[1]):
                au = self.__alfa(u, c.shape[0])
                av = self.__alfa(v, c.shape[1])
                s = self.__f(u, v)
                c[u, v] = au*av*s
        return c


    def idct(self):
        print("Calculando transformada inversa do cosseno...")
        f = np.zeros((self.img.shape))
        for x in range(f.shape[0]):
            print(x)
            for y in range(f.shape[1]):
                s = 0
                for u in range(self.img.shape[0]):
                    for v in range(self.img.shape[1]):
                        au = self.__alfa(u, self.img.shape[0])
                        av = self.__alfa(v, self.img.shape[1])
                        s += au * av * self.img[u, v]*self.__cosDCT(x, u, self.img.shape[0]) * \
                            self.__cosDCT(y, v, self.img.shape[1])
                f[x, y] = s
        return f

    def showImg(self, title):
        cv.imshow(title, self.img)
        k = cv.waitKey(0) & 0xFF
        if k == 27 or k == ord('q'):
            cv.destroyAllWindows()

    def __f(self, u, v):
        s = 0
        for x in range(self.img.shape[0]):
            for y in range(self.img.shape[1]):
                s += self.img[x, y] * self.__cosDCT(x, u, self.img.shape[0]) * \
                    self.__cosDCT(y, v, self.img.shape[1])
        return s

    def __alfa(self, u, N):
        if u == 0:
            return np.sqrt(1./N)
        elif u > 0:
            return np.sqrt(2./N)

    def __cosDCT(self, x, u, N):
        return np.cos(((2.*x+1)*u*np.pi)/(2*N))
