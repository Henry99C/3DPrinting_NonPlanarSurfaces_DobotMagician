import DobotDllType as dType
api = dType.load()
# Two possible movements: 4-Joint Mode, angle only move and 5-Linear Mode, straight path


def moveLinear(tetha, alpha, beta, gama, epsilon):
    dType.SetPTPCmdEx(api, 5, tetha, alpha, beta, epsilon, 0)
    duty_cycle = (gama * (1 / 100) + 1.5) * 5
    dType.SetIOPWM(api, 11, 50, duty_cycle, 0)
    print(f"Angles sent in Linear Mode: {tetha}, {alpha}, {beta}, {gama}, {epsilon}")


def moveJoint(tetha, alpha, beta, gama, epsilon):
    dType.SetPTPCmdEx(api, 4, tetha, alpha, beta, epsilon, 0)
    duty_cycle = (gama * (1 / 100) + 1.5) * 5
    dType.SetIOPWM(api, 11, 50, duty_cycle, 0)
    print(f"Angles sent in Joint Mode: {tetha}, {alpha}, {beta}, {gama}, {epsilon}")
