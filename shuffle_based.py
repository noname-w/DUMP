import math
import random
import copy
import numpy as np

# randomize real data with GRR mechanism
def randomized_response(data, k, p):
    for idx, num in enumerate(data):
        randomized_value = num
        if random.random() > p:
            while randomized_value == num:
                randomized_value = np.random.randint(0, k)
        data[idx] = randomized_value

def shuffle_based(data, k, epsilon, delta):
    n = len(data)

    # if epsilon out of the valid range, there is no amplification effect
    if epsilon > math.sqrt(14 * k * math.log(2 / delta) / (n - 1)):
        epsilon_l = math.log((epsilon**2) * (n-1) / (14 * math.log(2 / delta)) + 1 - k)
    else:
        epsilon_l = epsilon
    
    # randomize real data to satisfy ldp
    p = math.exp(epsilon_l) / (math.exp(epsilon_l) + k - 1)
    q = 1 / (math.exp(epsilon_l) + k - 1)
    randomized_response(data, k, p)

    # estimation
    freq = np.zeros(k, dtype = int)
    freq = (np.bincount(data) - q * n) / (p - q)
    
    return freq

def compute_mse(data, k, epsilon, delta, nround):
    n = len(data)
    error = 0
    true_freq = np.bincount(data)

    # run nround times to compute the MSE
    for r in range(nround):
        pre_freq = shuffle_based(copy.deepcopy(data), k, epsilon, delta)
        error += np.square((true_freq - pre_freq) / n).sum()   
    error = error / (k * nround)

    return error