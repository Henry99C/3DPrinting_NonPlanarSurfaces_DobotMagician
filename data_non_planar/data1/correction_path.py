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
input_file_name = os.path.join(output_path, 'puntos_editables.txt')

# Coordinates and vectors are abstracted from the editable points file
with open(input_file_name, 'r') as input_file:
    next(input_file)
    for line in input_file:
        values = linea.strip().split(', ')
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])
        i = float(values[3])
        j = float(values[4])
        k = float(values[5])

        original_coordinates.append((x, y, z))
        original_vectors.append((i, j, k))

cont = 0
# Intermediate points are eliminated
for coord in original_coordinates:
    x, y, z = coord

    if round(x) != 20.0 and round(x) != -20.0:
        original_coordinates.pop(cont)
        original_vectors.pop(cont)

    cont += 1


# The vector of corner coordinates is modified and the first 19 points are ignored
cont = 0
for coord, vec in zip(original_coordinates, original_vectors):

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

        coordinates_edited_1.append((x, y, z))
        vectors_edited_1.append((i, j, k))

    else:
        cont += 1
        pass

# 7 points are added, leaving a 5 mm pitch
for i in range(len(coordenadas_editadas_1)-1):
    x_1, y_1, z_1 = coordinates_edited_1[i]
    x_2, y_2, z_2 = coordinates_edited_1[i+1]

    i, j, k = vectors_edited_1[i]

    coordinates_edited_2.append((x_1, y_1, z_1))
    vectors_edited_2.append((i, j, k))

    if(round(x_1) == 20.0 and round(y_1) == 20.0)  and (round(x_2) == -20.0 and round(y_2) == 20.0):
        for m in range(1,4,1):
            coordinates_edited_2.append((x_1 - 5*m, y_1, z_1))
            vectors_edited_2.append((i, j, k))
        for m in range(4, 9,1):
            coordinates_edited_2.append((x_1 - 5*m, y_2, z_2))
            vectors_edited_2.append((i, j, k))

    if (round(x_1) == -20.0 and round(y_1) == -20.0) and (round(x_2) == 20.0 and round(y_2) == -20.0):
        for m in range(1, 4, 1):
            coordinates_edited_2.append((x_1 + 5*m, y_1, z_1))
            vectors_edited_2.append((i, j, k))
        for m in range(4, 9, 1):
            coordinates_edited_2.append((x_1 + 5*m, y_2, z_2))
            vectors_edited_2.append((i, j, k))

output_file_name = os.path.join(output_path, 'points_edited.txt')

with open(output_file_name, 'w') as output_file:
    output_file.write("X Y Z i j k\n")
    for coord, vec in zip(coordinates_edited_2, vectors_edited_2):
        line = f"{coord[0]}, {coord[1]}, {coord[2]}, {vec[0]}, {vec[1]}, {vec[2]}\n"
        output_file.write(line)

vertices, triangles = read_obj(os.path.join(current_path, 'custom_base.obj'), 40, 50)

plot_curved_path_vector(coordinates_edited_2, vectors_edited_2, vertices, triangles, type='plot', base_view=True)
