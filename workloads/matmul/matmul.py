import time
import sys
import numpy as np


def matmul(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    s = time.time()
    C = np.matmul(A, B)
    latency = time.time() - s
    return latency


def f(n):
    start = round(time.time(),6)
    result = matmul(int(n))
    end = round(time.time(),6)

if __name__ == "__main__":
    event = sys.argv[1]
    f(event)