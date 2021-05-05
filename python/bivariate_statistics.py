from scipy import stats
import numpy as np

def bivariate_statistics(data):


    if (len(data)!= 2) or (len(data[0])<=1):
        raise IndexError

    output = []
    stat = stats.stats.describe(data)
    mean = stat[2]
    var = stat[3]
    min,max = stat[1]
    stan_dev = np.sqrt(var)
    output.append(np.sum)


    return np.array(output)
