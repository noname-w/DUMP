import numpy as np
import math
import random
import copy
import xxhash

def olh(data, k, epsilon, delta):
    n = len(data)
    # compute optimal size of hash domain
    m = epsilon**2 * (n-1) / (14 * np.log(2 / delta))
    d = np.floor((m + 2) / 3)
    
    #compute local privacy budget, out of range has no privacy amplification
    epsilon_l = epsilon**2 * (n - 1) / (14 * np.log(2 / delta)) + 1 - d
    if epsilon_l < 1:
        epsilon_l = epsilon
    else:
        epsilon_l = np.log(epsilon_l)

    p = np.exp(epsilon_l) / (np.exp(epsilon_l) + d - 1)
    #q = 1 / (np.exp(epsilon_l) + d - 1)

    for i in range(n):
        v = data[i]
        x = (xxhash.xxh32(str(v), seed=i).intdigest() % d)
        y = x

        if random.random() > p:
            while y == x:
                y = np.random.randint(0, d)

        data[i] = y

    #estimate randimized data
    pre_freq = np.zeros(k, dtype = int)
    for i in range(n):
        for v in range(k):
            if data[i] == (xxhash.xxh32(str(v), seed=i).intdigest() % d):
                pre_freq[v] += 1
    a = 1.0 * d / (p * d - 1)
    b = 1.0 * n / (p * d - 1)
    pre_freq = a * pre_freq - b

    return pre_freq

def compute_mse(data, k, epsilon, delta, nround):
    n = len(data)
    error = 0
    true_freq = np.bincount(data)

    for r in range(nround):
        pre_freq = olh(copy.deepcopy(data), k, epsilon, delta)
        error += np.square((true_freq - pre_freq) / n).sum()   
    error = error / (k * nround)

    return error