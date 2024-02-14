import numpy as np


def valores_posibles(arreglo, lim_inf, lim_sup):
    # Se inicializa una arreglo para almacenar los valores filtrados
    valores_filtrados = []

    # Se eliminan los valores NaN y los valores que están por fuera de los limites
    for valor in arreglo:
        if not np.isnan(valor) and lim_inf <= valor <= lim_sup:
            valores_filtrados.append(round(valor, 4))

    # Se inicializa un arreglo para almacenar los valores sin que se repitan
    valores_unicos = []

    # Se almacenan los ángulos una única vez
    for valor in valores_filtrados:
        if valor not in valores_unicos:
            valores_unicos.append(valor)

    return valores_unicos


def valores_posibles_J2_J3(j2, j3):
    # Se inicializa una arreglo para almacenar los valores filtrados de J2
    valores_filtrados_j2 = []

    # Se filtran los valores de J2 eliminando los NaN y los que no son alcanzables
    for valor in j2:
        if not np.isnan(valor) and 0 <= valor <= 90:
            valores_filtrados_j2.append(round(valor, 4))

    # Se inicializa un arreglo para almacenar los valores de J2 sin que se repitan
    valores_unicos_j2 = []

    # Se almacenan los valore de J2 una única vez
    for valor in valores_filtrados_j2:
        if valor not in valores_unicos_j2:
            valores_unicos_j2.append(valor)

    # Se inicializa un arreglo para almacenar los valores de J3 sin que se repitan
    valores_unicos_j3 = []

    # Se eliminan los valores NaN de J3
    j3_sin_nan = np.nan_to_num(j3)

    # Se almacenan los valores de J3 una única vez
    for valor in j3_sin_nan:
        if valor not in valores_unicos_j3:
            valores_unicos_j3.append(valor)

    # Se inicializa una arreglo para almacenar [J2+J3, J2, J3]
    j23 = []

    # Se almacenan todas las combinaciones de [J2+J3, J2, J3]
    for valor_j2 in valores_unicos_j2:
        for valor_j3 in valores_unicos_j3:
            j23.append([valor_j2+valor_j3, valor_j2, valor_j3])

    # Se asignan valores de None a J23_filtrado, J2, J3 como precaución a que no exista una solución
    valores_filtrados_j23 = None
    J2 = None
    J3 = None

    #  Se obtiene el valor de J2 y J3, de revisar si J23 es alcanzable
    for valor in j23:
        if -10 <= valor[0] <= 85:
            valores_filtrados_j23 = round(valor[0], 4)
            J2 = round(valor[1], 4)
            J3 = round(valor[2], 4)
            break

    return J2, J3, valores_filtrados_j23

