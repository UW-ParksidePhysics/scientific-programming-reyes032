import numpy as np


def quadratic_fit(array):

    x_values = array[0, :]
    y_values = array[1, :]

    quadratic_coefficients = np.polyfit(x_values, y_values, 3)

    return quadratic_coefficients
