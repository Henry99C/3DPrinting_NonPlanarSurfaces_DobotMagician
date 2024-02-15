import numpy as np
import os
from viewer_path import plot_planar_path

# An empty matrix is initialized to store the coordinates
coordinates = []

# A variable is initialized to store the z value of each layer
z_current = None

# Full path to G-code file
current_path = os.path.join(os.path.dirname(__file__), 'data3')
gcode_name = os.path.join(current_path, 'custom_base_solid_09.gcode')
output_path = os.path.join(current_path, 'output')


# Open the G-code file
with open(gcode_name, "r") as file:
    for linea in file:
        words = line.split()
        # Check lines containing the word G0 or G1
        if words and (words[0] == "G0" or words[0] == "G1"):
            x, y, z = None, None, None
            for word in words:
                # Find the X, Y, Z components
                if word.startswith("X"):
                    x = float(word[1:])
                elif word.startswith("Y"):
                    y = float(word[1:])
                elif word.startswith("Z"):
                    if len(word) > 1:
                        z = float(word[1:])

            if x is not None and y is not None:
                if z is None:
                    z = z_current
                coordinates.append([x, y, z])
                z_current = z

output_file_name = os.path.join(output_path, 'coordinates.txt')

# The coordinates are stored in a txt file
with open(output_file_name, "w") as txt_file:
    for coordinate in coordinates:
        txt_file.write(f"{coordinate[0]:.3f}, {coordinate[1]:.3f}, {coordinate[2]:.1f}\n")

print(f"The coordinates have been stored in: '{output_file_name}'")

# An empty matrix is initialized to store the transformed coordinates.
coordinates_transformed = []

# The BST (Slicer with respect to the Base) transformation matrix is defined 
BST = np.array([[1, 0, 0, 79+100],
                [0, 1, 0, -(79+28.5)],
                [0, 0, 1, 32],
                [0, 0, 0, 1]])

for coordinate in coordinates:
    coordinate = [coordinate[0], coordinate[1], coordinate[2], 1]
    coordinate_transformed = np.dot(BST, coordinate)
    coordinates_transformed.append([coordinate_transformed[0], coordinate_transformed[1], coordinate_transformed[2]])

output_file_name = os.path.join(output_path, 'coordinatesTransformed.txt')

# The transformed coordinates are stored in a txt file
with open(output_file_name, "w") as txt_file:
    for coordinate in coordinates_transformed:
        txt_file.write(f"{coordinate[0]:.3f}, {coordinate[1]:.3f}, {coordinate[2]:.1f}, [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]\n")

print(f"The transformed coordinates have been stored in: '{output_file_name}'")

# An empty matrix is initialized to store the increased coordinates
increased_coordinates = []

for i in range(len(coordinates_transformed) - 1):
    increased_coordinates.append(coordinates_transformed[i])

    # The distance between the current point and the next point is calculated
    x1, y1, z1 = coordinates_transformed[i]
    x2, y2, z2 = coordinates_transformed[i + 1]
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

    # If the distance is greater than 5 mm, the points are increased
    if distance > 5:
        number_points = int(distancia / 5)
        step = [(x2 - x1) / (number_points + 1), (y2 - y1) / (number_points + 1), (z2 - z1) / (number_points + 1)]
        for j in range(numero_puntos):
            new_x = x1 + step[0] * (j + 1)
            new_y = y1 + step[1] * (j + 1)
            new_z = z1 + step[2] * (j + 1)
            increased_coordinates.append([new_x, new_y, new_z])

output_file_name = os.path.join(ruta_output, 'coordinatesIncreasedTransformed.txt')

# The increased and transformed coordinates are stored in a txt file
with open(output_file_name, "w") as txt_file:
    for coordinate in increased_coordinates:
        txt_file.write(f"{coordinate[0]:.3f}, {coordinate[1]:.3f}, {coordinate[2]:.1f}, [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]\n")

print(f"The augmented coordinates have been stored in: '{output_file_name}'")

plot_planar_path(coordinates_transformed, increased_coordinates, type='scatter')
