import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def plot_curved_path_rotation_matrix(coordinates, rotations_matrix, vertices, triangles, type):
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]
    z_coords = [coord[2] for coord in coordinates]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.add_collection3d(Poly3DCollection(vertices[triangles-1], facecolors='gray', linewidths=0.1, edgecolors='black', alpha=0.4))

    colors = ['r', 'g', 'b']

    R_original = np.eye(3)
    for i in range(3):
        X, Y, Z = R_original[0, i], R_original[1, i], R_original[2, i]
        ax.quiver(0, 0, 0, X, Y, Z, color=colors[i], linestyle='--', alpha=0.5, arrow_length_ratio=0.1)

    n = 0
    for rotation in rotations_matrix:
        for i in range(3):
            origin = coordinates[n]
            X, Y, Z = origin
            U, V, W = rotation[0, i], rotation[1, i], rotation[2, i]
            ax.quiver(X, Y, Z, U, V, W, color=colors[i], arrow_length_ratio=0.1)
        n += 1

    if type == 'plot':
        ax.plot(x_coords, y_coords, z_coords, c='orange')
    elif type == 'scatter':
        ax.scatter(x_coords, y_coords, z_coords, c='b', marker='.')
    else:
        ax.plot(x_coords, y_coords, z_coords, c='orange')

    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])
    ax.set_zlim([0, 80])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(0, 90)

    plt.show()


def plot_curved_path_vector(coordinates, vectors, vertices, triangles, type, base_view):
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]
    z_coords = [coord[2] for coord in coordinates]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if base_view == True:
        ax.add_collection3d(Poly3DCollection(vertices[triangles - 1], facecolors='gray', linewidths=0.1, edgecolors='black', alpha=0.4))

    colors = ['r', 'g', 'b']

    R_original = np.eye(3)
    for i in range(3):
        X, Y, Z = R_original[0, i], R_original[1, i], R_original[2, i]
        ax.quiver(0, 0, 0, X, Y, Z, color=colors[i], linestyle='--', alpha=0.5, arrow_length_ratio=0.1)

    for index, vec in enumerate(vectors):
        coord = coordinates[index]
        ax.quiver(coord[0], coord[1], coord[2], vec[0], vec[1], vec[2], color='red', length=1, normalize=True)

    if type == 'plot':
        ax.plot(x_coords, y_coords, z_coords, c='orange')
    elif type == 'scatter':
        ax.scatter(x_coords, y_coords, z_coords, c='b', marker='.')
    else:
        ax.plot(x_coords, y_coords, z_coords, c='orange')

    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])
    ax.set_zlim([0, 80])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(0,0)

    plt.show()


def plot_planar_path(coordinates_transformed, increased_coordinates, type):
    x_coords = [coord[0] for coord in coordinates_transformed]
    y_coords = [coord[1] for coord in coordinates_transformed]
    z_coords = [coord[2] for coord in coordinates_transformed]

    x_coords_inc = [coord[0] for coord in increased_coordinates]
    y_coords_inc = [coord[1] for coord in increased_coordinates]
    z_coords_inc = [coord[2] for coord in increased_coordinates]

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, projection='3d')

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, projection='3d')

    if type == 'plot':
        ax1.plot(x_coords, y_coords, z_coords, c='orange')
        ax2.plot(x_coords_inc, y_coords_inc, z_coords_inc, linestyle='dashed', c='b')
    elif type == 'scatter':
        ax1.scatter(x_coords, y_coords, z_coords, c='b', marker='.')
        ax2.scatter(x_coords_inc, y_coords_inc, z_coords_inc, c='r', marker='.')
    else:
        ax1.plot(x_coords, y_coords, z_coords, c='orange')
        ax2.plot(x_coords_inc, y_coords_inc, z_coords_inc, linestyle='dashed', c='b')
    ax1.set_title('Coordenadas Originales')

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')

    ax1.set_xlim([np.min(x_coords), np.max(x_coords)])
    ax1.set_ylim([np.min(y_coords), np.max(y_coords)])
    ax1.set_zlim([np.min(z_coords), np.max(z_coords)])

    ax2.set_title('Coordenadas Aumentadas')

    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')

    ax2.set_xlim([np.min(x_coords_inc), np.max(x_coords_inc)])
    ax2.set_ylim([np.min(y_coords_inc), np.max(y_coords_inc)])
    ax2.set_zlim([np.min(z_coords_inc), np.max(z_coords_inc)])

    plt.show()


def both_path(coordinates_base, coordinates_geom, type):
    x_coords_base = [coord[0] for coord in coordinates_base]
    y_coords_base = [coord[1] for coord in coordinates_base]
    z_coords_base = [coord[2] for coord in coordinates_base]

    x_coords_geom = [coord[0] for coord in coordinates_geom]
    y_coords_geom = [coord[1] for coord in coordinates_geom]
    z_coords_geom = [coord[2] for coord in coordinates_geom]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if type == 'plot':
        ax.plot(x_coords_base, y_coords_base, z_coords_base, label='base', linestyle='dashed', c='blue')
        ax.plot(x_coords_geom, y_coords_geom, z_coords_geom, label='geometria', c='red')
    elif type == 'scatter':
        ax.scatter(x_coords_base, y_coords_base, z_coords_base, label='base', c='blue', marker='.')
        ax.scatter(x_coords_geom, y_coords_geom, z_coords_geom, label='geometria', c='red', marker='.')
    else:
        ax.plot(x_coords_base, y_coords_base, z_coords_base, label='base', linestyle='dashed', c='blue')
        ax.plot(x_coords_geom, y_coords_geom, z_coords_geom, label='geometria', c='red')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim([np.min(x_coords_base), np.max(x_coords_base)])
    ax.set_ylim([np.min(y_coords_base), np.max(y_coords_base)])
    ax.set_zlim([np.min(z_coords_base), np.max(z_coords_geom)])

    ax.legend()

    ax.view_init(elev=0, azim=0)

    plt.show()
