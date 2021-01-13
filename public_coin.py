import numpy as np
import math
import random
import xxhash
import copy

def public_coin(data, k, epsilon, delta):
    # public parameters
    n = len(data)
    tau_ = math.ceil(np.log(2 * k))
    s = 2 * n
    gamma_ = 90 * tau_**2 * np.log(2 * tau_ / delta) / (n * epsilon**2)

    # public randomness
    hash_family = np.random.randint(0, 1.0e8, tau_) #select tau_ hash functions

    # encode
    T = np.zeros([tau_, s], dtype = int)

    for j, value in enumerate(data): # encode data
        for t, seed_ in enumerate(hash_family):
            h = xxhash.xxh32(str(value), seed=seed_).intdigest() % s 
            T[t, h] += 1

    for t in range(tau_): #add noise
        for l in range(s):
            T[t, l] += np.random.binomial(n, gamma_)
    
    # decode
    pre_fre = np.zeros(k, dtype = int)

    for value in range(k):
        min_ = 2 * n + 1
        for t, seed_ in enumerate(hash_family):
            h = xxhash.xxh32(str(value), seed=seed_).intdigest() % s
            if min_ > T[t, h]:
                min_ = T[t, h]
        pre_fre[value] = max(min_ - gamma_ * n, 0)

    return pre_fre

def compute_mse(data, k, epsilon, delta, nround):   
    n = len(data)
    error = 0
    true_freq = np.bincount(data)

    # run nround times to compute the MSE
    for r in range(nround):
        pre_freq = public_coin(copy.deepcopy(data), k, epsilon, delta)
        error += np.square((true_freq - pre_freq) / n).sum()
    error = error / (k * nround)

    return error