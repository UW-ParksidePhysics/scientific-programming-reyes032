import numpy as np
from equations_of_state import fit_eos
from two_column_text_read import two_column_text_read
from byvariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
import matplotlib.pyplot as plt
from plot_data_with_fit import plot_data_with_fit




def parse_file_name(file_name):
    names = file_name.split(".")
    chemical_symbol = names[0]
    crystal_symetery = names[1]
    d_f_c_a = names[2]
    return chemical_symbol, crystal_symetery, d_f_c_a


array = two_column_text_read("Ag.Fm-3m.GGA-PBE.volumes_energies.dat")


stats = bivariate_statistics(array)
#print(stats)

quadratic_coefficients = quadratic_fit(array)
volumes = array[0, :]
energies = array[1, :]
fit_eos_array, fit_parameters = fit_eos(volumes, energies, quadratic_coefficients, eos="murnaghan", number_of_points=50)

bulk_modulus = fit_parameters[1]
equilibrium_volume = fit_parameters[3]

# Define an array of fit volumes going from volumes[0] to volumes[-1] but equal in number of points to fit_eos_array

plt.plot(volumes, energies, 'bo')
plt.plot(fit_volumes, fit_eos_array, 'k')
plt.xlabel(r'$\mathit{V}(\AA^3$/atom)')
plt.ylabel(r'$\mathit{E}$ (eV/atom)')


plt.show()

