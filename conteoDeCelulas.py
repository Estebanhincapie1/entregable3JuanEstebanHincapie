# IMPORTAMOS LAS LIBRERIAS

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# LEEMOS LA IMAGEN DE LA QUE QUEREMOS CONTAR LAS IMAGENES
imagen = cv.imread('cell.jpg')

# CAMBIAMOS EL COLOR A GRISES
imagengrises = cv.cvtColor(imagen,cv.COLOR_BGR2GRAY)
cv.imshow('Grises',imagengrises)
cv.waitKey(0)
cv.destroyAllWindows()

# UMBRALIZAMOS LA IMAGEN 
umb,uminv=cv.threshold(imagengrises,0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow('umbralizacion',uminv)
cv.waitKey(0)
cv.destroyAllWindows()

# PRIMERO HAY QUE DILATAR LA IMAGEN

# creamos el kernel
kernel = np.ones((5,5), np.uint8)

# aplicamos la dilatacion con 1 iteraciones
imaDilatada = cv.dilate(uminv, kernel, iterations = 1)

# SEGUNDO HAY QUE EROSIONARLA CON EL MISMO KERNEL
imaErosionada = cv.erode(imaDilatada,kernel,iterations = 10) 
plt.imshow(imaErosionada, cmap='gray')
plt.title('Erosionada')
plt.show()

# CONTAMOS LOS ELEMENTOS
elementos,mask = cv.connectedComponents(imaErosionada)

print(elementos)
