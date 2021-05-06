

def plot_data_with_fit(data, fit_curve, data_format="", fit_format=""):

    import matplotlib.pyplot as plt
    curve_plot = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
    scatter_plot = plt.scatter(data[0, :], data[1, :], data_format)
    plt.show()
    return curve_plot, scatter_plot
