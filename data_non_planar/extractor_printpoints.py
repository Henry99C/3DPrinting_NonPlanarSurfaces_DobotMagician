import os
import json
from readObj import read_obj
from viewer_path import plot_curved_path_vector

# An array is initialized to store coordinates and vectors
coordinates = []
vectors = []

# Enter the offset to center the part
offsetX = 50
offsetY = 50

# Se ingresa la ruta de los archivos
current_path = os.path.dirname(__file__)
data_path = os.path.join(current_path, 'data7_3')
output_path = os.path.join(data_path, 'output')
json_file_name = os.path.join(data_path, "out_printpoints.json")

# The JSON points delivered by Compas Slicer are loaded
with open(json_file_name, 'r') as json_file:
    data = json.load(json_file)

# Enter the name of the output file
output_file_name = os.path.join(output_path, 'coordinates_vectors.txt')

# The coordinates and vectors of the JSON file are stored in the respective array
with open(output_file_name, 'w') as output_file:
    output_file.write("X Y Z i j k\n")
    for key, value in data.items():

        point = value['point']
        x, y, z = point
        up_vector = value['up_vector']
        i, j, k = up_vector

        line = f"{x:.4f}, {y:.4f}, {z:.4f}, {i:.4f}, {j:.4f}, {k:.4f}\n"
        output_file.write(line)

        coordinates.append((x-offsetX, y-offsetY, z))
        vectors.append((i, j, k))

print(f"The coordinates and vectors have been stored in: {output_file_name}.")

output_file_name = os.path.join(output_path, 'editable_points.txt')

# Store each point and its corresponding vector with offset in a file for postprocessing
with open(output_file_name, 'w') as output_file:
    output_file.write("X Y Z i j k\n")
    for coord, vec in zip(coordenadas, vectores):
        x, y, z = coord
        i, j, k = vec
        line = f"{x:.4f}, {y:.4f}, {z:.4f}, {i:.4f}, {j:.4f}, {k:.4f}\n"
        output_file.write(line)

print(f"The editable coordinates and vectors have been stored in: {nombre_archivo_salida}.")

vertices, triangles = read_obj(os.path.join(data_path, 'custom_base.obj'), offsetX, offsetY)
plot_curved_path_vector(coordinates, vectors, vertices, triangles, type='plot', base_view=True)
