from ecuaciones_cinematica_inversa import CalcTheta1, CalcTheta2, CalcTheta3, CalcTheta5, CalcTheta6
from filtro_angulos import valores_posibles, valores_posibles_J2_J3
import os

# Se inicializa una matriz vacá para almacenar coordenadas, ángulos y marcos
coordenadas = []
angulos = []
marcos = []

# Paremetros D-H
l0 = 138
l1 = 135
l2 = 147
l3 = 125.61
l4 = 79.5

# Se ingresa la ruta de los archivos
carpeta_actual = os.path.dirname(__file__)
tipo_impresion = os.path.join(carpeta_actual, 'data_non_planar')
ruta_data = os.path.join(tipo_impresion, 'data8')
ruta_output = os.path.join(ruta_data, 'output')
nombre_archivo_entrada = os.path.join(ruta_output, 'coordenadasTransformadas_marcos.txt')

# Se almacenan las coordenadas y marcos en las matrices
with open(nombre_archivo_entrada, 'r') as archivo_entrada:
    for linea in archivo_entrada:
        x, y, z, matriz_str = linea.strip().split(",", 3)
        coordenadas.append([float(x), float(y), float(z)])
        marcos.append(eval(matriz_str))

# Se realiza el calculo de la cinematica pose a pose
for i in range(0, len(coordenadas)):
    x = coordenadas[i][0]
    y = coordenadas[i][1]
    z = coordenadas[i][2]
    rd = marcos[i]
    try:
        J6 = valores_posibles(CalcTheta6(rd), -85, 85)[0]
        J5 = valores_posibles(CalcTheta5(rd), -20, 80)[0]
        J1 = valores_posibles(CalcTheta1(x, y, l4, J6), -135, 135)[0]
        J2, _, J3 = valores_posibles_J2_J3(CalcTheta2(x, z, l0, l1, l2, l3, l4, J1, J5, J6),
                                          CalcTheta3(x, z, l0, l1, l2, l3, l4, J1, J5, J6))
    except IndexError:
        print(i)
        print(f"{J6}, {J5}, {J3}, {J2}, {J1}")
        J6, J5, J3, J2, J1 = [None, None, None, None, None]
        print("Error: No existe solucion para esta POSE.")

    # print(f"Axis J1:{J1}, Axis J2:{J2}, Axis J3:{J3}, Axis J5:{J5}, Axis J6:{J6}")
    angulos.append([J1, J2, J3, J5, J6])

# Ruta del archivo de salida
nombre_archivo_salida = os.path.join(ruta_output, 'valores_angulos.txt')

# Se almacenan los angulos
with open(nombre_archivo_salida, "w") as archivo_salida:
    archivo_salida.write("J1 J2 J3 J5 J6\n")

    for angulo in angulos:
        angulo_str = " ".join([str(a) if isinstance(a, float) else f"[{', '.join(map(str, a))}]" for a in angulo])
        archivo_salida.write(f"{angulo_str}\n")

print(f"Los valores de los ángulos han sido almacenados en: '{nombre_archivo_salida}'")
