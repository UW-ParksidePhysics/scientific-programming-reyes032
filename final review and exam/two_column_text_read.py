"""
This function reads in two columns of data from a text file of arbitrary length. It returns the data as columns
of an array with x values in row 1 and the corresponding y value in row 2. the length of the array is determined
by the length of the input file.
"""

__author__ = "Michael Luccas & Cheo Reyes"

import numpy as np


def two_column_text_read(file_name):

    try:
        file = open(file_name)
    except OSError as error:
        print(error)
        return

    content = file.readlines()
    data = np.zeros([2, (len(content))], float)
    n = 0

    for line in content:
        elements = line.split()
        data[0, n] = float(elements[0])
        data[1, n] = float(elements[1])
        n += 1

    return data
