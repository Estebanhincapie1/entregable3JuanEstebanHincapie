import pydicom
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

# Ruta de la carpeta que contiene las imágenes DICOM
carpeta_imagenes = 'imagenes/'

archivos = os.listdir(carpeta_imagenes)

archivos_dicom = [archivo for archivo in archivos if archivo.endswith('.dcm')]

# Mostrar cada imagen en una ventana de Matplotlib en cascada
for archivo_dicom in archivos_dicom:
    # Cargar el archivo DICOM
    ds = pydicom.dcmread(os.path.join(carpeta_imagenes, archivo_dicom))

    # Obtener la imagen
    imagen = ds.pixel_array

    plt.figure()

    # Mostrar la imagen en la ventana actual
    plt.imshow(imagen, cmap=plt.cm.gray)
    plt.title(archivo_dicom)  
    plt.axis('off')  


plt.show()

