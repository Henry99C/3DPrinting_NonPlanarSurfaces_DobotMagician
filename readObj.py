import numpy as np


def read_obj(filename, offset_x, offset_y):
    vertices = []
    triangles = []

    with open(filename) as file:
        for line in file:
            components = line.strip().split()
            if components:
                if components[0] == 'v':
                    if components[0] == 'v':
                        vertex = [float(i) for i in components[1:]]
                        vertex[0] -= offset_x
                        vertex[1] -= offset_y
                        vertices.append(vertex)
                elif components[0] == 'f':
                    triangles.append([int(i.split('//')[0]) for i in components[1:]])
    return np.array(vertices, dtype=float), np.array(triangles, dtype=int)
