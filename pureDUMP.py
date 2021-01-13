import math
import copy
import numpy as np

# generate dummy points uniformly and randomly
def gen_dummy(n, s, k):
    dummy_set = np.random.randint(0, k, math.ceil(n*s))
    return dummy_set

def pure_dummy (data, k, epsilon, delta):
    n = len(data)
    # compute the number of dummy data
    s = (14 * k * math.log(2/delta) / (epsilon**2) + 1 ) / n

    # generate dummy data
    dummy_set = gen_dummy(n, s, k)
    # get shuffled data
    shuffled_data = np.append(data, dummy_set)

    # estimation
    freq = np.zeros(k, dtype = int)
    freq = np.bincount(shuffled_data) - math.ceil(n * s) / k

    return freq

def compute_mse(data, k, epsilon, delta, nround):
    n = len(data)
    error=0
    true_freq = np.bincount(data)

    # run nround times to compute the MSE
    for r in range(nround): 
        pre_freq = pure_dummy(copy.deepcopy(data), k, epsilon, delta)
        error += np.square((pre_freq - true_freq) / n).sum()
    error = error/(k * nround)

    return error