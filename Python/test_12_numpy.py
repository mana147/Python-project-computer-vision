from builtins import len
import matplotlib.pyplot as plt
import numpy as np
import collections
import time


def void(name):
    if not name:
        print("--------------------------------")
    else:
        print("---------" + name + "-----------")


# ---------------------------------------------------------------------

vector_a = np.array(['a', 100, 'b', 'c', 11, 90, 'str', 10])
vector_b = np.array([['v', 0,  1, 99, 6], ['b', 2,  5, 00, 7]])
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
# ---------------------------------------------------------------------

void("data A")
print(A)

print("data:", A[1:1])
print("kieu du lieu", A.dtype)  # kieu du lieu
print("so hang , so cot ", A.shape)  # so hang va cot
print("chuyen vi matran", A.T)  # chuyen vi ma tran

print("ravel", A.ravel())
# ---------------------------------------------------------------------

void("re_shape")
re_A = A.reshape(1, 12)
print(re_A)


void("")


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


meno = {0: 5, 6: 9}

print(meno)
