"""
This function
"""

__author__ = "Michael Luccas & Cheo Reyes"


def bivariate_statistics(data):

    from scipy import stats
    import numpy as np

    if (len(data) != 2) or (len(data[0]) <= 1):
        raise IndexError

    data = data.T
    stat = stats.describe(data)
    mean = stat.mean
    var = stat.variance
    xy_min, xy_max = stat.minmax
    stan_dev = np.sqrt(var)
    output = [mean[1], stan_dev[1], xy_min[0], xy_max[0], xy_min[1], xy_max[1]]
    return np.array(output)
