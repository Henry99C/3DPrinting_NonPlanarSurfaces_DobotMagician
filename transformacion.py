import os
import numpy as np
from rotation import rotationX, rotationY, rotationZ
from readObj import read_obj
from viewer_path import plot_curved_path_rotation_matrix

# Se inicializa un arreglo para almacenar las coordenada, vectores, matrices de rotacion y las coordenadas transformadas
coordenadas = []
vectores = []
matriz_rotacion = []
coordenadas_transformadas = []

# Se ingresa el offset para centrar la pieza
offsetX = 50
offsetY = 50

# Se ingresa la ruta de los archivos
carpeta_actual = os.path.dirname(__file__)
ruta_data = os.path.join(carpeta_actual, 'data7_3')
ruta_output = os.path.join(ruta_data, 'output')
nombre_archivo_entrada = os.path.join(ruta_output, "puntos_editables.txt")

# Se obtienen las coordenadas y los vectores del archivo puntos editables/ puntos editados
with open(nombre_archivo_entrada, 'r') as archivo_entrada:
    next(archivo_entrada)
    for linea in archivo_entrada:
        values = linea.strip().split(', ')
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])
        i = float(values[3])
        j = float(values[4])
        k = float(values[5])

        coordenadas.append((x, y, z))
        vectores.append((i, j, k))

# Se calcula la matriz de rotacion para cada uno de los vectores
for vector in vectores:
    magnitud_vector = np.round(np.linalg.norm(vector), 5)
    vx, vy, vz = vector

    if magnitud_vector != 1:
        vector = (vx/magnitud_vector, vy/magnitud_vector, vz/magnitud_vector)
        vx, vy, vz = vector
        magnitud_vector = np.round(np.linalg.norm(vector), 5)

    theta_y = np.round(np.rad2deg(np.arccos(vy / magnitud_vector)), 5)
    theta_x = np.round(np.rad2deg(np.arctan2(-vz, -vx)), 5)

    R_x = rotationX(180)
    R_y = rotationY(theta_x)
    R_z = rotationZ(90-theta_y)

    R = np.dot(R_x, np.dot(R_y, R_z))

    matriz_rotacion.append(R)

nombre_archivo_salida = os.path.join(ruta_output, 'coordenadas_marcos.txt')

# Se almacenan los marcos y las coordenadas sin transformar
with open(nombre_archivo_salida, 'w') as output_file:
    output_file.write("X Y Z Matriz de rotación\n")
    for coordenada, rotacion in zip(coordenadas, matriz_rotacion):
        rotacion_formateada = ", ".join([f"[{columna[0]}, {columna[1]}, {columna[2]}]" for columna in rotacion])
        output_file.write(f"{coordenada[0]}, {coordenada[1]}, {coordenada[2]}, [{rotacion_formateada}]\n")

print(f"Las coordenadas y las matrices de rotacion han sido almacenadas en: '{nombre_archivo_salida}'.")

# Se define la matriz de transformación (BST: Base Slicer Transform)
BST = np.array([[1, 0, 0, 79+100+110],
                [0, 1, 0, 0],
                [0, 0, 1, 32],
                [0, 0, 0, 1]])

# Se aplica la transformación a las coordenadas
for coordenada in coordenadas:
    coordenada = [coordenada[0], coordenada[1], coordenada[2], 1]
    coordenada_transformada = np.dot(BST, coordenada)
    coordenadas_transformadas.append([coordenada_transformada[0], coordenada_transformada[1], coordenada_transformada[2]])

nombre_archivo_salida = os.path.join(ruta_output, 'coordenadasTransformadas_marcos.txt')

# almacenan los marcos y las coordenadas transformadas
with open(nombre_archivo_salida, 'w') as archivo_salida:
    for coordenada, rotacion in zip(coordenadas_transformadas, matriz_rotacion):
        rotacion_formateada = ", ".join([f"[{columna[0]}, {columna[1]}, {columna[2]}]" for columna in rotacion])
        archivo_salida.write(f"{coordenada[0]}, {coordenada[1]}, {coordenada[2]}, [{rotacion_formateada}]\n")

print(f"Las coordenadas transformadas y las matrices de rotacion han sido almacenadas en: '{nombre_archivo_salida}'.")

vertices, triangulos = read_obj(os.path.join(ruta_data, 'custom_base.obj'), offsetX, offsetY)

plot_curved_path_rotation_matrix(coordenadas, matriz_rotacion, vertices, triangulos, type='plot')