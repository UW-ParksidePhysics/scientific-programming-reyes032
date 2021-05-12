import numpy as np
from equations_of_state import fit_eos
from two_column_text_read import two_column_text_read
from byvariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
import matplotlib.pyplot as plt
from plot_data_with_fit import plot_data_with_fit

#def parse_file_name(filename):
    #filename = "Ag.Fm-3m.GGA-PBE.volumes_energies.dat"
    #content = filename
    ##for line in content:
    #    name =
    #    return name



array = two_column_text_read("Ag.Fm-3m.GGA-PBE.volumes_energies.dat")


stats = bivariate_statistics(array)


quadratic_coefficients = quadratic_fit(array)


vinet = fit_eos(array[0], array[1], quadratic_coefficients)

volumes = array[0]
energies = array[1]

plt.plot(volumes, energies, 'bo')
plt.plot(vinet, 'k')
plt.xlabel(r'$\mathit{V}(\AA^3$/atom)')
plt.ylabel(r'$\mathit{E}$ (eV/atom)')
plt.show()
