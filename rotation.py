import numpy as np


def rotationX(tetha_x):
    tetha = np.radians(tetha_x)
    R_x = np.array([[1, 0, 0], [0, np.cos(tetha), -np.sin(tetha)], [0, np.sin(tetha), np.cos(tetha)]])
    return np.round(R_x, 9)


def rotationY(tetha_y):
    tetha = np.radians(tetha_y)
    R_y = np.array([[np.cos(tetha), 0, np.sin(tetha)], [0, 1, 0], [-np.sin(tetha), 0, np.cos(tetha)]])
    return np.round(R_y, 9)


def rotationZ(tetha_z):
    tetha = np.radians(tetha_z)
    R_z = np.array([[np.cos(tetha), -np.sin(tetha), 0], [np.sin(tetha), np.cos(tetha), 0], [0, 0, 1]])
    return np.round(R_z, 9)