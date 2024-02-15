import numpy as np


def possible_values(array, low_bound, upper_bound):
    # An array is initialized to store the filtered values
    filtered_values = []

    # NaN values and values outside the limits are eliminated
    for value in array:
        if not np.isnan(value) and low_bound <= value <= upper_bound:
            filtered_values.append(round(value, 4))

    # An array is initialized to store the values without repeating them
    unique_values = []

    # Angles are stored only once
    for value in filtered_values:
        if value not in unique_values:
            unique_values.append(value)

    return unique_values


def possible_values_J2_J3(j2, j3):
    # An array is initialized to store the filtered values of J2
    filtered_values_j2 = []

    # J2 values are filtered by eliminating NaN and those that are not achievable
    for value in j2:
        if not np.isnan(value) and 0 <= value <= 90:
            filtered_values_j2.append(round(value, 4))

    # An array is initialized to store the values of J2 without repeating them.
    unique_values_j2 = []

    # J2 values are stored only once
    for value in filtered_values_j2:
        if value not in unique_values_j2:
            unique_values_j2.append(value)

    # An array is initialized to store the values of J3 without repeating them
    unique_values_j3 = []

    # NaN values of J3 are eliminated
    j3_no_nan = np.nan_to_num(j3)

    #  The values of J3 are stored only once
    for value in j3_no_nan:
        if value not in unique_values_j3:
            unique_values_j3.append(value)

    # An array is initialized to store [J2+J3, J2, J3]
    j23 = []

    # All combinations of [J2+J3, J2, J3] are stored
    for value_j2 in unique_values_j2:
        for value_j3 in unique_values_j3:
            j23.append([value_j2+value_j3, value_j2, value_j3])

    # Values of None are assigned to J23_filtering, J2, J3 as a precaution that there is no solution.
    filtered_values_j23 = None
    J2 = None
    J3 = None

    #  The value of J2 and J3 is obtained, to check if J23 is achievable.
    for value in j23:
        if -10 <= value[0] <= 85:
            filtered_values_j23 = round(value[0], 4)
            J2 = round(value[1], 4)
            J3 = round(value[2], 4)
            break

    return J2, J3, filtered_values_j23
