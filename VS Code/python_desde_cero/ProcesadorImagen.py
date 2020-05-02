import matplotlib as plt
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image


tom_and_jerry_image = Image.open("Tom_and_Jerry.jpg")

#Se hace un array de la imagen 
image1 = np.array(tom_and_jerry_image)

#se ponen la forma de la imagen 2500 x 1500 x 3
row_x, colu_y, layersTotal = image1.shape

#se le pone los indices de todas las filas y columnas
x, y = np.ogrid[:row_x,:colu_y]

#sacar el punto central de la fila y la columna en 
center_x1, center_y1 = int(row_x*.66), int(colu_y*.33)
center_x2, center_y2 = int(row_x*.33), int(colu_y*.66)

dot_uno = (x - center_x1)**2 + (y - center_y1)**2
dot_dos = (x - center_x2)**2 + (y - center_y2)**2

#sacar el radio del circulo
circle_1 = (100)**2
circle_2 = (150)**2

circle_Mask1 = (dot_uno < circle_1)
circle_Mask2 = (dot_dos < circle_2)

image1[circle_Mask1 + circle_Mask2]=0

im = Image.fromarray(image1)
im.save("Tom_and_JerryModificado.jpg")