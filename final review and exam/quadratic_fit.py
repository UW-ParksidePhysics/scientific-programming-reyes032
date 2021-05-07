"""
This function accepts an array of x and y data and returns the coefficients of the second order quadratic equation
which best represents y values as a function of x values
"""

__author__ = "Michael Luccas & Cheo Reyes"

import numpy as np


def quadratic_fit(array):

    x_values = array[0, :]
    y_values = array[1, :]

    quadratic_coefficients = np.polyfit(x_values, y_values, 2)

    return quadratic_coefficients
