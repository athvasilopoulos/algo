"""
Maximum Sub-array Sum Problem
O(n^2) algorithm with holding array
"""
import time
import random


def zero_list_maker(n):
    C = [0] * n
    return C


def max_subarray(A, B):
    start_t = time.time()
    m = partialsum = start = end = 0
    length = len(B)
    for i in range(0, length):
        if i == 0:
            B[i] = A[i]
        else:
            B[i] = B[i - 1] + A[i]
    for start_index in range(0, length):
        for end_index in range(start_index, length):
            if i == 0:
                partialsum = B[end_index]
            else:
                partialsum = B[end_index] - B[start_index - 1]
            if partialsum > m:
                m = partialsum
                start = start_index
                end = end_index
    Ret = [m, start, end]
    print("Elapsed time = %.3f s" % (time.time() - start_t))
    return Ret


A = []
print("For the array with the 5000 elements:")
random.seed(1053578)
for i in range(5000):
    A.append(random.randint(-100, 100))
B = zero_list_maker(5000)
C = max_subarray(A, B)
print("The maximum sum is %d " % C[0])
print("The start index is %d " % C[1])
print("The end index is %d " % C[2])
print("")

A = []
print("For the array with the 10000 elements:")
random.seed(1053578)
for i in range(10000):
    A.append(random.randint(-100, 100))
G = zero_list_maker(10000)
C = max_subarray(A, G)
print("The maximum sum is %d " % C[0])
print("The start index is %d " % C[1])
print("The end index is %d " % C[2])
