import math
import numpy as np
from scipy.linalg import hadamard

def codeword_gen(k):
    codewords = np.empty([2 * k - 1, k], dtype = int)
    hadamard_ = hadamard(2 * k)
    
    for value in range(2 * k - 1): # the first row in hadamard cannot be used
        codeword = 0
        for index in range(2 * k): # select idex of 1 per row, half of values equal to 1 per row
            if hadamard_[value + 1, index] == 1:
                codewords[value, codeword] = index # save the index as the hadamard codeword
                codeword += 1
    
    return codewords

def private_coin(data, k, codewords, epsilon, delta):
    n = len(data)
    rho = math.ceil(36 * math.log(1 / (delta)) / (epsilon**2))
    tau = math.ceil(math.log2(n))

    data_encoded = np.zeros([n + n * rho, tau], dtype = int)

    # encode data  
    for data_idex in range(n):
        for codeword_idex in range(tau):
            data_encoded[data_idex, codeword_idex] = codewords[data[data_idex], np.random.randint(0, k)]
    
    for rho_idex in range(n, n + rho * n):
        data_encoded[rho_idex] = np.random.randint(0, 2 * k, tau)

    # decode data
    data_encoded_size = rho * n + n
    freq = np.zeros(k, dtype = int)
    for item in range(k):
        for idex in range(data_encoded_size):
            if set(data_encoded[idex]) <= set(codewords[item]):
                freq[item] += 1

    pre_freq = (freq - (rho + 1) * n / np.power(2, tau)) / (1 - 1 / np.power(2, tau))

    return pre_freq

def compute_mse(data, k, codewords, epsilon, delta, nround):
    n = len(data)
    error = 0
    true_freq = np.bincount(data)

    for r in range(nround):
        pre_freq = private_coin(data, k, codewords, epsilon, delta)
        error += np.square((pre_freq - true_freq) / n).sum()

    error = error / (k * nround)
    
    return error