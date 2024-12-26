import numpy as np
import os
import cv2

# TODO: Restructure the code
def cargar_datos_y_etiquetas():
    imagenes = []
    etiquetas = []
    for idx, clase in enumerate(clases):
        ruta_clase = os.path.join(ruta_base, clase)
        for archivo in os.listdir(ruta_clase):
            img = cv2.imread(os.path.join(ruta_clase, archivo))
            img = img / 255.0  # Normalización
            imagenes.append(img)
            etiquetas.append(idx)
    return np.array(imagenes), np.array(etiquetas)