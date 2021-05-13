from generate_matrix import generate_matrix
from lowest_egienvector import lowest_eigenvector
import matplotlib.pyplot as plt
import numpy as np
potential_name = 'sinusoidal'
number_of_dimensions = 90
potential_parameter = 300

matrix = generate_matrix(-10, 10, number_of_dimensions, potential_name, potential_parameter)

eigenvectors = lowest_eigenvector(matrix, 3)
#print(eigenvectors)

x = np.linspace(-10, 10, number_of_dimensions)
plt.plot(x,eigenvectors[0])
plt.xlabel("x [a.u.]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.axhline(color="black")
plt.text( "Created by Cheo Reyes May/12/21")
plt.title("Select Wavefunctions for a Sinusoidal Potential on a Spatial Grid of 2, 3, 4 Points")
