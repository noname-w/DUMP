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

# generate dummy points uniformly and randomly
def gen_dummy(n, s, k):
    dummy_set = np.random.randint(0, k, math.ceil(n * s))
    return dummy_set

def mix_dummy(data, k, epsl, epsilon, delta):
    n=len(data)
    p = math.exp(epsl) / (math.exp(epsl) + k - 1)
    q = 1 / (math.exp(epsl) + k - 1)
    
    # randomize real data
    randomized_response(data, k, p)

    # compute the number of dummy data
    lambda_ = k / ((math.exp(epsl) + k - 1) * (k - 1))
    s = (14 * k * math.log(4 / delta) / (epsilon**2) + 1 + math.sqrt(2 * (n - 1) * lambda_ * math.log(2 / delta)) - (n - 1) * lambda_) / n

    # generate dummy data
    dummy_set = gen_dummy(n, s, k)
    # get shuffled data
    shuffled_data = np.append(data, dummy_set)

    # estimation
    freq = np.zeros(k, dtype = int)
    freq = (np.bincount(shuffled_data) - n * q - (math.ceil(n * s)) / k) / (p - q)

    return freq

def compute_mse(data, k, epsilon, delta, epsilon_l, nround):
    n = len(data)
    error=0
    true_freq = np.bincount(data)

    # run nround times to compute the MSE
    for r in range(nround): 
        pre_freq = mix_dummy(copy.deepcopy(data), k, epsilon_l, epsilon, delta)
        error += np.square((pre_freq - true_freq) / n).sum()
    error = error / (k * nround)

    return error