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
print(stats)

quadratic_coefficients = quadratic_fit(array)

fit_eos_array = fit_eos(array[0], array[1], quadratic_coefficients, eos="vinet", number_of_points=50)
print(fit_eos_array)



plt.scatter(array[0], array[1], 'bo')
plt.plot(fit_eos_array, 'k')
plt.xlabel(r'$\mathit{V}(\AA^3$/atom)')
plt.ylabel(r'$\mathit{E}$ (eV/atom)')
plt.xlim([101.746523, 142.2979448])
plt.ylim([-316.060057,-258.5834622])
plt.show()


def annotate_graph():

