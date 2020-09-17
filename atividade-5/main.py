import numpy as np
import cv2 as cv
import sys
import os
from Operations import Operations

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


imgName = getArgs(sys.argv, '-i')
outputs = 'outputs/'


img = cv.imread('images/'+imgName, 0)
resize = 50
img = cv.resize(img, (resize, resize))


op = Operations(img)
print("============= Operacao dct =============")
dct = op.dct()
cv.imwrite(outputs+'dct.jpg', dct)
print('DCT salvo em: ' + outputs+'dct.jpg')

print("============= Filtro passsa baixa =============")
low = op.lowPass(dct, 20)
cv.imwrite(outputs+'passa-baixa.jpg', low)
print('Passa baixa salvo em: ' + outputs+'passa-baixa.jpg')

print("============= Filtro passsa alta =============")
high = op.highPass(dct, 20)
cv.imwrite(outputs+'passa-alta.jpg', high)
print('Passa alta salvo em: ' + outputs+'passa-alta.jpg')
# exit()
print("============= Transformada Cosseno em passsa baixa =============")
low_idct = op.idct(low)
cv.imwrite(outputs+'cos-passa-baixa.jpg', low_idct)
print('Trans cosseno passa baixa salvo em: ' + outputs+'cos-passa-baixa.jpg')

print("============= Transformada Cosseno em passsa alta =============")
high_idct = op.idct(high)
cv.imwrite(outputs+'cos-passa-alta.jpg', high_idct)
print('Trans cosseno passa alta salvo em: ' + outputs+'cos-passa-alta.jpg')

noise = cv.imread(outputs+'ruido-1.jpg')
nl = op.lowPass(noise, 20)
nh = op.highPass(noise, 20)
noise_low_idct = op.idct(nl)
noise_high_idct = op.idct(nh)
cv.imwrite(outputs+'noise-low-idct.jpg', noise_low_idct)
cv.imwrite(outputs+'noise-high-idct.jpg', noise_high_idct)

