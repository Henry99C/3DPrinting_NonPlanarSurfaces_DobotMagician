import DobotDllType as dType
from moveDobot import moveJoint
import os

api = dType.load()
ruta_actual = os.path.dirname(__file__)

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError: "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

state = dType.ConnectDobot(api, "COM6", 115200)[0]

print("Connect status:", CON_STR[state])

if state == dType.DobotConnect.DobotConnect_NoError:

    # Homing
    print("Home...")

    dType.SetHOMEParams(api, 250, 0, 40, 0, isQueued=0)
    dType.SetHOMECmd(api, temp=0, isQueued=0)
    
    # Se ajusta velocidad y aceleración de las articulaciones para la impresion
    dType.SetPTPJointParams(api, 50, 10, 50, 10, 50, 10, 50, 10, 0)

    # Se configura la Interfaz E/S
    dType.SetIOMultiplexing(api, 10, 1, 0)
    dType.SetIOMultiplexing(api, 11, 2, 0)
    dType.SetIOMultiplexing(api, 12, 1, 0)
    dType.dSleep(100)

    dType.SetIODO(api, 10, 1, 0)
    dType.SetIODO(api, 12, 1, 0)
    dType.dSleep(100)

    # Se inicia la extrusión de material
    dType.SetEMotor(api, 0, 1, 180, 0)
    dType.dSleep(100)

    # Se ingresa la ruta de la superficie plana a imprimir
    tipo_impresion = os.path.join(ruta_actual, "data_non_planar")
    ruta_data = os.path.join(tipo_impresion, "data9")
    ruta_output = os.path.join(ruta_data, "output")
    nombre_archivo = os.path.join(ruta_output, "valores_angulos.txt")
    print(f"Imprimiendo :{nombre_archivo}")

    with open(nombre_archivo, 'r') as file:
        next(file)
        for line in file:
            angles = line.split()
            moveJoint(float(angles[0]), float(angles[1]), float(angles[2]), float(angles[3]), float(angles[4]))

    ultimaPosicion = dType.GetPose(api)
    dType.SetPTPCmdEx(api, 2, ultimaPosicion[0], ultimaPosicion[1], ultimaPosicion[2]+3, ultimaPosicion[3], 0)

    # Se apagan la interfaz E/S y se detiene la extrusión
    dType.SetIODO(api, 10, 0, 0)
    dType.SetIODO(api, 12, 0, 0)
    dType.SetEMotorS(api, 0, 0, 0, 0, 0)

dType.DisconnectDobot(api)
