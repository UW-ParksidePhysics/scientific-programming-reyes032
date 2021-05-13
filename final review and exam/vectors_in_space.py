from generate_matrix import generate_matrix
from lowest_egienvector import lowest_eigenvector
import matplotlib.pyplot as plt
import numpy as np
potential_name = 'sinusoidal'
number_of_dimensions = 90
potential_parameter = 300

matrix = generate_matrix(-10, 10, number_of_dimensions, potential_name, potential_parameter)

eigenvalues, eigenvectors = lowest_eigenvector(matrix, 4)
print(eigenvectors)

x = np.linspace(-10, 10, number_of_dimensions)
for n in range(2,5):
    plt.plot(x,eigenvectors[n])

plt.xlabel("x [a.u.]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.axhline(color="black")
plt.text(-10.69, -.22, "Created by Cheo Reyes May/12/21")
plt.title("Select Wavefunctions for a Sinusoidal Potential on a Spatial Grid of 2, 3, 4 Points")
plt.show()


if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Reyes.Sinusoidal.Eigenvector2, 3, 4.png")
