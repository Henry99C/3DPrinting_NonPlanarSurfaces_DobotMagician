import os
import json
from readObj import read_obj
from viewer_path import plot_curved_path_vector

# Se inicializa un arreglo para almacenar las coordenada y vectores
coordenadas = []
vectores = []

# Se ingresa el offset para centrar la pieza
offsetX = 50
offsetY = 50

# Se ingresa la ruta de los archivos
carpeta_actual = os.path.dirname(__file__)
ruta_data = os.path.join(carpeta_actual, 'data7_3')
ruta_output = os.path.join(ruta_data, 'output')
nombre_archivo_json = os.path.join(ruta_data, "out_printpoints.json")

# Se cargan los puntos del JSON entregado por Compas Slicer
with open(nombre_archivo_json, 'r') as archivo_json:
    data = json.load(archivo_json)

# Se ingresa el nombre del archivo de salida
nombre_archivo_salida = os.path.join(ruta_output, 'coordenadas_vectores.txt')

# Se almacenan las coordenadas y vectores del archvio JSON, en el respectivo arreglo
with open(nombre_archivo_salida, 'w') as archivo_salida:
    archivo_salida.write("X Y Z i j k\n")
    for key, value in data.items():

        point = value['point']
        x, y, z = point
        up_vector = value['up_vector']
        i, j, k = up_vector

        linea = f"{x:.4f}, {y:.4f}, {z:.4f}, {i:.4f}, {j:.4f}, {k:.4f}\n"
        archivo_salida.write(linea)

        coordenadas.append((x-offsetX, y-offsetY, z))
        vectores.append((i, j, k))

print(f"Las coordenadas y vectores han sido almacenadas en: {nombre_archivo_salida}.")

nombre_archivo_salida = os.path.join(ruta_output, 'puntos_editables.txt')

# Store each point and its corresponding vector with offset in a file for postprocessing
with open(nombre_archivo_salida, 'w') as output_file:
    output_file.write("X Y Z i j k\n")
    for coord, vec in zip(coordenadas, vectores):
        x, y, z = coord
        i, j, k = vec
        line = f"{x:.4f}, {y:.4f}, {z:.4f}, {i:.4f}, {j:.4f}, {k:.4f}\n"
        output_file.write(line)

print(f"Las coordenadas y vectores editables han sido almacenadas en: {nombre_archivo_salida}.")

vertices, triangulos = read_obj(os.path.join(ruta_data, 'custom_base.obj'), offsetX, offsetY)
plot_curved_path_vector(coordenadas, vectores, vertices, triangulos, type='plot', base_view=True)