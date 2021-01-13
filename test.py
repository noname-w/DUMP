import numpy as np
import pureDUMP
import mixDUMP
import private_coin
import public_coin
import shuffle_based
import private_shuffle
import SOLH

def pureDUMP_test(data, k, epsilon, delta, nround):
    error = pureDUMP.compute_mse(data, k, epsilon, delta, nround)

    return error

def mixDUMP_test(data, k, epsilon, delta, epsilon_l, nround):
    error = mixDUMP.compute_mse(data, k, epsilon, delta, epsilon_l, nround)

    return error

def private_coin_test(data, k, epsilon, delta, nround):
    codewords = private_coin.codeword_gen(k)
    error = private_coin.compute_mse(data, k, codewords, epsilon, delta, nround)

    return error

def public_coin_test(data, k, epsilon, delta, nround):
    error = public_coin.compute_mse(data, k, epsilon, delta, nround)

    return error

def shuffle_based_test(data, k, epsilon, delta, nround):
    error = shuffle_based.compute_mse(data, k, epsilon, delta, nround)

    return error

def private_shuffle_test(data, k, epsilon, delta, nround):
    error = private_shuffle.compute_mse(data, k, epsilon, delta, nround)

    return error

def SOLH_test(data, k, epsilon, delta, nround):
    error = SOLH.compute_mse(data, k, epsilon, delta, nround)

    return error

def main():
    data = np.loadtxt('./dataset/test.txt', dtype = int)
    k = np.max(data)+1 # k=50 in test.txt
    n = len(data) # n=500,000 in test.txt
    epsilon = 0.5
    delta = 10e-6
    nround = 1
    epsilon_l = 8
    print('pureDUMP:', pureDUMP_test(data, k, epsilon, delta, nround))
    print('mixDUMP:', mixDUMP_test(data, k, epsilon, delta, epsilon_l, nround))
   # print('private_coin:', private_coin_test(data, k, epsilon, delta, nround)) # The running time is not acceptable
    print('public_coin:', public_coin_test(data, k, epsilon, delta, nround))
    print('shuffle_based:', shuffle_based_test(data, k, epsilon, delta, nround))
    print('private_shuffle:', private_shuffle_test(data, k, epsilon, delta, nround))
    print('SOLH:', SOLH_test(data, k, epsilon, delta, nround))

if __name__ == "__main__":
    main()