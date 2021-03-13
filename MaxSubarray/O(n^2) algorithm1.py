"""
Maximum Sub-array Sum Problem
O(n^2) algorithm without holding array
"""
import random
import time


def max_subarray(A):
    Ret = [-1000, 0, 0]
    length = len(A)
    start_t = time.time()
    for start in range(0, length):
        placeholder = 0
        for sub_size in range(1, length + 1):
            if start + sub_size > length:
                break
            placeholder += A[start + sub_size - 1]
            if placeholder > Ret[0]:
                Ret[0] = placeholder
                Ret[1] = start
                Ret[2] = start + sub_size - 1
    print("Elapsed time = %.3f s" % (time.time() - start_t))
    return Ret


A = []
print("For the array with the 5000 elements:")
random.seed(1053578)
for i in range(5000):
    A.append(random.randint(-100, 100))
B = max_subarray(A)
print("The maximum sum is %d " % B[0])
print("The start index is %d " % B[1])
print("The end index is %d " % B[2])
print("")

print("For the array with the 10000 elements:")
A = []
random.seed(1053578)
for i in range(10000):
    A.append(random.randint(-100, 100))
B = max_subarray(A)
print("The maximum sum is %d " % B[0])
print("The start index is %d " % B[1])
print("The end index is %d " % B[2])
