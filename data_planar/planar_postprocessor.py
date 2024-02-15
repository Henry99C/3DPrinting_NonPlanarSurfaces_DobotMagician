import numpy as np
import os
from viewer_path import plot_planar_path

# Se inicializa una matriz vacía para almacenar las coordenadas
coordenadas = []

# Se inicializa una variable para almacenar el valor de z de cada capa
z_actual = None

# Ruta completa al archivo G-code
ruta_actual = os.path.join(os.path.dirname(__file__), 'data3')
gcode_nombre = os.path.join(ruta_actual, 'custom_base_solid_09.gcode')
ruta_output = os.path.join(ruta_actual, 'output')


# Abrir el archivo G-code
with open(gcode_nombre, "r") as archivo:
    for linea in archivo:
        palabras = linea.split()
        #Revisa las lineas que contengan la palabra G0 o G1
        if palabras and (palabras[0] == "G0" or palabras[0] == "G1"):
            x, y, z = None, None, None
            for palabra in palabras:
                # Encuentra las componentes X, Y, Z
                if palabra.startswith("X"):
                    x = float(palabra[1:])
                elif palabra.startswith("Y"):
                    y = float(palabra[1:])
                elif palabra.startswith("Z"):
                    if len(palabra) > 1:
                        z = float(palabra[1:])

            if x is not None and y is not None:
                if z is None:
                    z = z_actual
                coordenadas.append([x, y, z])
                z_actual = z

nombre_archivo_salida = os.path.join(ruta_output, 'coordenadas.txt')

# Se almacenan las coordenas en un archivo txt
with open(nombre_archivo_salida, "w") as archivo_txt:
    for coordenada in coordenadas:
        archivo_txt.write(f"{coordenada[0]:.3f}, {coordenada[1]:.3f}, {coordenada[2]:.1f}\n")

print(f"Las coordenadas han sido almacenadas en '{nombre_archivo_salida}'")

# Se inicializa una matriz vacía para almacenar las coordenadas transformadas
coordenadas_transformadas = []

# Se define la matriz de transformación BST (Slicer con respecto a la Base)
BST = np.array([[1, 0, 0, 79+100],
                [0, 1, 0, -(79+28.5)],
                [0, 0, 1, 32],
                [0, 0, 0, 1]])

for coordenada in coordenadas:
    coordenada = [coordenada[0], coordenada[1], coordenada[2], 1]
    coordenada_transformada = np.dot(BST, coordenada)
    coordenadas_transformadas.append([coordenada_transformada[0], coordenada_transformada[1], coordenada_transformada[2]])

nombre_archivo_salida = os.path.join(ruta_output, 'coordenadasTransformadas.txt')

# Se almacenan las coordenadas transformadas en un archivo txt
with open(nombre_archivo_salida, "w") as archivo_txt:
    for coordenada in coordenadas_transformadas:
        archivo_txt.write(f"{coordenada[0]:.3f}, {coordenada[1]:.3f}, {coordenada[2]:.1f}, [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]\n")

print(f"Las coordenadas transformadas han sido almacenadas en '{nombre_archivo_salida}'")

# Se inicializa una matriz vacía para almacenar las coordenadas aumentadas
coordenadas_aumentadas = []

for i in range(len(coordenadas_transformadas) - 1):
    coordenadas_aumentadas.append(coordenadas_transformadas[i])

    # Se calcula la distancia entre el punto actual y el siguiente
    x1, y1, z1 = coordenadas_transformadas[i]
    x2, y2, z2 = coordenadas_transformadas[i + 1]
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

    # Si la distancia es mayor a 5 mm se aumentan los puntos
    if distancia > 5:
        numero_puntos = int(distancia / 5)
        paso = [(x2 - x1) / (numero_puntos + 1), (y2 - y1) / (numero_puntos + 1), (z2 - z1) / (numero_puntos + 1)]
        for j in range(numero_puntos):
            nueva_x = x1 + paso[0] * (j + 1)
            nueva_y = y1 + paso[1] * (j + 1)
            nueva_z = z1 + paso[2] * (j + 1)
            coordenadas_aumentadas.append([nueva_x, nueva_y, nueva_z])

nombre_archivo_salida = os.path.join(ruta_output, 'coordenadasAumentadasTransformadas.txt')

# Se almacenan las coordenadas aumentadas y transformadas en un archivo txt
with open(nombre_archivo_salida, "w") as archivo_txt:
    for coordenada in coordenadas_aumentadas:
        archivo_txt.write(f"{coordenada[0]:.3f}, {coordenada[1]:.3f}, {coordenada[2]:.1f}, [[0, 0, -1], [0, -1, 0], [-1, 0, 0]]\n")

print(f"Las coordenadas aumentadas han sido almacenadas en: '{nombre_archivo_salida}'")

plot_planar_path(coordenadas_transformadas, coordenadas_aumentadas, type='scatter')
