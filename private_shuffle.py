import math
import random
import copy
import numpy as np

def randomize_hist(data, k, true_freq, epsilon, delta):
    n = len(data)
    randomize_freq = np.zeros(k, dtype = int)

    p = 1 - 50 * math.log(2 / delta) / ((epsilon**2) * n)
    if p < 0:
        p = 0
    
    # each user may send each element even he doesn't hold this element
    for i in range(k):
        randomize_freq[i] = true_freq[i] + np.random.binomial(n, p)

    # the condition in the paper. The result will turn to bad if consider it.
    '''
    pre_freq = np.zeros(k, dtype = int) 
    for i in range(k):
        if randomize_freq[i] - n * p < 0:
            pre_freq[i] = randomize_freq[i] - n * p
    '''
    pre_freq = randomize_freq - n * p
    return pre_freq

def compute_mse(data, k, epsilon, delta, nround):
    n = len(data)
    error = 0
    true_freq = np.bincount(data)

    for r in range(nround):
        pre_freq = randomize_hist(copy.deepcopy(data), k, true_freq, epsilon, delta)
        error += np.square((pre_freq - true_freq) / n).sum()
    error = error / (k * nround)

    return error