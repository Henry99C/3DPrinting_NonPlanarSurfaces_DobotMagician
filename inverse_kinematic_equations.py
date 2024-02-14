import numpy as np


def CalcTheta6(rd):
    # print("THETA 6")
    # OPTION 1
    s6 = rd[2][1]
    c6 = -rd[2][0]
    theta6_1 = np.rad2deg(np.arctan2(s6, c6))
    # print(f"Theta 6-1: {theta6_1}")
    # OPTION 2
    s6 = rd[1][2]*rd[0][0] - rd[0][2]*rd[1][0]
    c6 = rd[1][2]*rd[0][1] - rd[0][2]*rd[1][1]
    theta6_2 = np.rad2deg(np.arctan2(s6, c6))
    # print(f"Theta 6-2: {theta6_2}")
    theta6 = [theta6_1, theta6_2]
    return theta6


def CalcTheta5(rd):
    # print("THETA 5")
    # OPTION 1
    s5 = -rd[2][2]
    c5 = np.sqrt(rd[2][0]**2 + rd[2][1]**2)
    theta5_1 = np.rad2deg(np.arctan2(s5, c5))
    # print(f"Theta 5-1: {theta5_1}")
    # OPTION 2
    s5 = -rd[2][2]
    c5 = -np.sqrt(rd[2][0]**2 + rd[2][1]**2)
    theta5_2 = np.rad2deg(np.arctan2(s5, c5))
    # print(f"Theta 5-2: {theta5_2}")
    # OPTION 3
    s5 = -rd[2][2]
    c5 = np.sqrt(rd[0][2]**2 + rd[1][2]**2)
    theta5_3 = np.rad2deg(np.arctan2(s5, c5))
    # print(f"Theta 5-3: {theta5_3}")
    # OPTION 4
    s5 = -rd[2][2]
    c5 = -np.sqrt(rd[0][2]**2 + rd[1][2]**2)
    theta5_4 = np.rad2deg(np.arctan2(s5, c5))
    # print(f"Theta 5-4: {theta5_4}")
    theta5 = [theta5_1, theta5_2, theta5_3, theta5_4]
    return theta5


def CalcTheta1(x, y, l4, theta6):
    # print("THETA 1")
    # OPTION 1
    theta1_1 = np.rad2deg(2*np.arctan((-x + np.sqrt(x**2 + y**2 - (l4**2)*(np.sin(np.deg2rad(theta6))**2)))/(y - l4*np.sin(np.deg2rad(theta6)))))
    # print(f"Theta 1-1: {theta1_1}")
    # OPTION 2
    theta1_2 = np.rad2deg(2*np.arctan((-x - np.sqrt(x**2 + y**2 - (l4**2)*(np.sin(np.deg2rad(theta6))**2)))/(y - l4*np.sin(np.deg2rad(theta6)))))
    # print(f"Theta 1-2: {theta1_2}")
    theta1 = [theta1_1, theta1_2]
    return theta1


def CalcTheta2(x, z, l0, l1, l2, l3, l4, theta1, theta5, theta6):
    # print("THETA 2")
    a = ((x - l4*np.sin(np.deg2rad(theta1))*np.sin(np.deg2rad(theta6))) / np.cos(np.deg2rad(theta1))) - l3 - l4*np.sin(np.deg2rad(theta5))*np.cos(np.deg2rad(theta6))
    b = z - l0 + l4*np.cos(np.deg2rad(theta5))*np.cos(np.deg2rad(theta6))
    c3 = (a ** 2 + b ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
    # print(f"Cos(theta3)={c3}")
    s3 = np.sqrt(1 - c3 ** 2)
    # print(f"Sin(theta3)={s3}")
    theta2_1 = np.rad2deg(np.arctan2(-b, a)) - np.rad2deg(np.arctan((l2 * s3) / (l1 + l2 * c3))) + 90
    # print(f"Theta 2-1: {theta2_1}")
    theta2_2 = np.rad2deg(np.arctan2(-b, a)) - np.rad2deg(np.arctan((-l2 * s3) / (l1 + l2 * c3))) + 90
    # print(f"Theta 2-2: {theta2_2}")
    tetha2 = [theta2_1, theta2_2]

    return tetha2


def CalcTheta3(x, z, l0, l1, l2, l3, l4, theta1, theta5, theta6):
    # print("THETA 3")
    a = ((x - l4*np.sin(np.deg2rad(theta1))*np.sin(np.deg2rad(theta6))) / np.cos(np.deg2rad(theta1))) - l3 - l4*np.sin(np.deg2rad(theta5))*np.cos(np.deg2rad(theta6))
    b = z - l0 + l4*np.cos(np.deg2rad(theta5))*np.cos(np.deg2rad(theta6))
    c3 = (a ** 2 + b ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
    # print(f"Cos(theta3)={c3}")
    s3 = np.sqrt(1 - c3 ** 2)
    # print(f"Sin(theta3)={s3}")
    theta3_1 = np.rad2deg(np.arctan2(s3, c3)) - 90
    # print(f"Theta 3-2: {theta3_1}")
    theta3_2 = np.rad2deg(np.arctan2(-s3, c3)) - 90
    # print(f"Theta 3-1: {theta3_2}")
    theta3 = [theta3_1, theta3_2]
    return theta3
