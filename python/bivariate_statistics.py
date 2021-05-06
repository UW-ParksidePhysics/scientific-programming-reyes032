from scipy import stats
import numpy as np


# import two_coloum_text as tc


def bivariate_statistics(data):
    if (len(data) != 2) or (len(data[0]) <= 1):
        raise IndexError

    data = data.T
    stat = stats.describe(data)
    mean = stat.mean
    var = stat.variance
    min, max = stat.minmax
    stan_dev = np.sqrt(var)
    # output.append(np.sum)
    # stat(tc)
    # Mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value
    output = [mean[1], stan_dev[1], min[0], max[0], min[1], max[1]]
    return np.array(output)


if __name__ == '__main__':
    x = [1, 2, 3]
    y = [4, 5, 6]
    data = np.array([x, y])
    output = bivariate_statistics(data)
    print(output)
