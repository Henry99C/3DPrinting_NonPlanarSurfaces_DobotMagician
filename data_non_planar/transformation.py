import os
import numpy as np
from rotation import rotationX, rotationY, rotationZ
from readObj import read_obj
from viewer_path import plot_curved_path_rotation_matrix

# An array is initialized to store the coordinates, vectors, rotation matrices and transformed coordinates
coordinates = []
vectors = []
rotation_matrix = []
coordinates_transformed = []

# Enter the offset to center the part
offsetX = 50
offsetY = 50

# Enter the path to the files
current_path = os.path.dirname(__file__)
data_path = os.path.join(current_path, 'data7_3')
output_path = os.path.join(data_path, 'output')
input_file_name = os.path.join(output_path, "editable_points.txt")

# Coordinates and vectors are obtained from the editable points/editable points file
with open(input_file_name, 'r') as input_file:
    next(input_file)
    for line in input_file:
        values = line.strip().split(', ')
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])
        i = float(values[3])
        j = float(values[4])
        k = float(values[5])

        coordinates.append((x, y, z))
        vectors.append((i, j, k))

# The rotation matrix is calculated for each of the vectors
for vector in vectors:
    vector_magnitude = np.round(np.linalg.norm(vector), 5)
    vx, vy, vz = vector

    if vector_magnitude != 1:
        vector = (vx/vector_magnitude, vy/vector_magnitude, vz/vector_magnitude)
        vx, vy, vz = vector
        vector_magnitude = np.round(np.linalg.norm(vector), 5)

    theta_y = np.round(np.rad2deg(np.arccos(vy / vector_magnitude)), 5)
    theta_x = np.round(np.rad2deg(np.arctan2(-vz, -vx)), 5)

    R_x = rotationX(180)
    R_y = rotationY(theta_x)
    R_z = rotationZ(90-theta_y)

    R = np.dot(R_x, np.dot(R_y, R_z))

    rotation_matrix.append(R)

output_file_name = os.path.join(output_path, 'frame_coordinates.txt')

# Frames and coordinates are stored without transformation
with open(output_file_name, 'w') as output_file:
    output_file.write("X Y Z Rotation matrix\n")
    for coordinate, rotation in zip(coordinates, rotation_matrix):
        rotation_formatted = ", ".join([f"[{row[0]}, {row[1]}, {row[2]}]" for row in rotation])
        output_file.write(f"{coordinate[0]}, {coordinate[1]}, {coordinate[2]}, [{rotation_formatted}]\n")

print(f"The coordinates and the rotation matrices have been stored in: '{nombre_archivo_salida}'.")

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
