import numpy as np
import cv2

img = cv2.imread('botellas.jpg')
img_g = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

forma = np.shape(img_g)

img2 = np.zeros(forma)

for x in list(range(1,forma[0]-1)):
    
    for y in list(range(1,forma[1]-1)):
        suma = 0

        for i in list(range(-1,2)):

            for j in list(range(-1,2)):
                suma = img_g[x-i,y-j] * kernel[i+1,j+1] + suma

        img2[x,y] = suma

max_s = np.max(img2)
img2 = img2*255/max_s
img2 = img2.astype(np.uint8)

cv2.imshow('Original',img_g)
cv2.imshow('Filtrada',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
