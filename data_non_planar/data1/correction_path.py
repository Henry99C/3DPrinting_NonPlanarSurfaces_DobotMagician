import os
import numpy as np
from readObj import read_obj
from viewer_path import plot_curved_path_vector

# Arrays are initialized to store the original and edited values
original_coordinates = []
original_vectors = []
coordinates_edited_1 = []
vectors_edited_1 = []
coordinates_edited_2 = []
vectors_edited_2 = []

# File paths
current_path = os.path.dirname(__file__)
output_path = os.path.join(current_path, 'output')
input_file_name = os.path.join(ruta_salida, 'puntos_editables.txt')

# Se abstraen las coordenadas y los vectores del archivo puntos editables
with open(nombre_archivo_entrada, 'r') as archivo_entrada:
    next(archivo_entrada)
    for linea in archivo_entrada:
        valores = linea.strip().split(', ')
        x = float(valores[0])
        y = float(valores[1])
        z = float(valores[2])
        i = float(valores[3])
        j = float(valores[4])
        k = float(valores[5])

        coordenadas_originales.append((x, y, z))
        vectores_originales.append((i, j, k))

cont = 0
# Se eliminan los puntos intermedios
for coord in coordenadas_originales:
    x, y, z = coord

    if round(x) != 20.0 and round(x) != -20.0:
        coordenadas_originales.pop(cont)
        vectores_originales.pop(cont)

    cont += 1


# Se modfica el vector de las coordenadas de las esquinas y se ignoran los primeros 19 puntos
cont = 0
for coord, vec in zip(coordenadas_originales, vectores_originales):

    if cont > 19:
        x, y, z = coord
        i, j, k = vec

        if z < 60:
            if np.round(x) == 20.0 and np.round(y) == 20.0:
                i = -0.0076
                j = 0.5488
                k = 0.8358

            elif np.round(x) == -20.0 and np.round(y) == 20.0:
                i = -0.0076
                j = 0.5488
                k = 0.8358

            elif np.round(x) == -20.0 and np.round(y) == -20.0:
                i = 0.0076
                j = -0.5488
                k = 0.8358

            elif np.round(x) == 20.0 and np.round(y) == -20.0:
                i = 0.0076
                j = -0.5488
                k = 0.8358

        coordenadas_editadas_1.append((x, y, z))
        vectores_editados_1.append((i, j, k))

    else:
        cont += 1
        pass

# Se agregan 7 puntos, lo cual deja un paso de 5 mm
for i in range(len(coordenadas_editadas_1)-1):
    x_1, y_1, z_1 = coordenadas_editadas_1[i]
    x_2, y_2, z_2 = coordenadas_editadas_1[i+1]

    i, j, k = vectores_editados_1[i]

    coordenadas_editadas_2.append((x_1, y_1, z_1))
    vectores_editados_2.append((i, j, k))

    if(round(x_1) == 20.0 and round(y_1) == 20.0)  and (round(x_2) == -20.0 and round(y_2) == 20.0):
        for m in range(1,4,1):
            coordenadas_editadas_2.append((x_1 - 5*m, y_1, z_1))
            vectores_editados_2.append((i, j, k))
        for m in range(4, 9,1):
            coordenadas_editadas_2.append((x_1 - 5*m, y_2, z_2))
            vectores_editados_2.append((i, j, k))

    if (round(x_1) == -20.0 and round(y_1) == -20.0) and (round(x_2) == 20.0 and round(y_2) == -20.0):
        for m in range(1, 4, 1):
            coordenadas_editadas_2.append((x_1 + 5*m, y_1, z_1))
            vectores_editados_2.append((i, j, k))
        for m in range(4, 9, 1):
            coordenadas_editadas_2.append((x_1 + 5*m, y_2, z_2))
            vectores_editados_2.append((i, j, k))

output_file_name = os.path.join(ruta_salida, 'puntos_editados.txt')

with open(output_file_name, 'w') as output_file:
    output_file.write("X Y Z i j k\n")
    for coord, vec in zip(coordenadas_editadas_2, vectores_editados_2):
        line = f"{coord[0]}, {coord[1]}, {coord[2]}, {vec[0]}, {vec[1]}, {vec[2]}\n"
        output_file.write(line)

vertices, triangulos = read_obj(os.path.join(carpeta_actual, 'custom_base.obj'), 40, 50)

plot_curved_path_vector(coordenadas_editadas_2, vectores_editados_2, vertices, triangulos, type='plot', base_view=True)
