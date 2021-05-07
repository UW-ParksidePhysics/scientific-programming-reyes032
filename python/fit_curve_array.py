"""
This function takes an input of the coefficients of a quadratic function and returns columns of an array
 with x values in row one and y values in row two. These values correspond to a fit curve representing a function
 of x with the given polynomial coefficients.
"""

__author__ = "Michael Luccas & Cheo Reyes"

import numpy as np


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_points=100):

    if max_x < min_x:
        raise ArithmeticError
    if number_points <= 2:
        raise IndexError

    x_array = np.linspace(min_x, max_x, number_points)
    y_array = np.polyval(quadratic_coefficients, x_array)
    data = np.array((x_array, y_array))  # np.column_stack((x_array, y_array))

    return data
