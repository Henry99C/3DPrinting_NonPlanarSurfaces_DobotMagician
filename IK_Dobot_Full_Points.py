from inverse_kinematic_equations import CalcTheta1, CalcTheta2, CalcTheta3, CalcTheta5, CalcTheta6
from angle_filter import possible_values, possible_values_J2_J3
import os

# An empty matrix is initialized to store coordinates, angles and frames.
coordinates = []
angles = []
frames = []

# Parameters D-H
l0 = 138
l1 = 135
l2 = 147
l3 = 125.61
l4 = 79.5

# Enter the path to the files
current_path = os.path.dirname(__file__)
print_type = os.path.join(current_path, 'data_non_planar')
data_path = os.path.join(print_type, 'data8')
output_path = os.path.join(data_path, 'output')
input_file_name = os.path.join(output_path, 'coordinatesTransformed_frames.txt')

# The coordinates and frames are stored in the matrices
with open(input_file_name, 'r') as input_file:
    for line in input_file:
        x, y, z, matriz_str = line.strip().split(",", 3)
        coordinates.append([float(x), float(y), float(z)])
        frames.append(eval(matriz_str))

# The calculation of the kinematics is performed pose by pose.
for i in range(0, len(coordinates)):
    x = coordinates[i][0]
    y = coordinates[i][1]
    z = coordinates[i][2]
    rd = frames[i]
    try:
        J6 = possible_values(CalcTheta6(rd), -85, 85)[0]
        J5 = possible_values(CalcTheta5(rd), -20, 80)[0]
        J1 = possible_values(CalcTheta1(x, y, l4, J6), -135, 135)[0]
        J2, _, J3 = possible_values_J2_J3(CalcTheta2(x, z, l0, l1, l2, l3, l4, J1, J5, J6),
                                          CalcTheta3(x, z, l0, l1, l2, l3, l4, J1, J5, J6))
    except IndexError:
        print(i)
        print(f"{J6}, {J5}, {J3}, {J2}, {J1}")
        J6, J5, J3, J2, J1 = [None, None, None, None, None]
        print("Error: There is no solution for this POSE")

    # print(f"Axis J1:{J1}, Axis J2:{J2}, Axis J3:{J3}, Axis J5:{J5}, Axis J6:{J6}")
    angles.append([J1, J2, J3, J5, J6])

# Output file path
output_file_name = os.path.join(output_path, 'angle_values.txt')

# Angles are stored
with open(output_file_name, "w") as output_file:
    output_file.write("J1 J2 J3 J5 J6\n")

    for angle in angles:
        angle_str = " ".join([str(a) if isinstance(a, float) else f"[{', '.join(map(str, a))}]" for a in angle])
        output_file.write(f"{angle_str}\n")

print(f"The values of the angles have been stored in: '{output_file_name}'")
