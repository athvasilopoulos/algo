"""
Maximum Sub-array Sum Problem
O(n) Kadane's algorithm
"""
import random
import time


def max_subarray(A):
    max_ending_here = A[0]
    start_old = start = end = max_so_far = 0
    start_t = time.time()
    for i, x in enumerate(A[1:], 1):
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            start = i + 1
        elif max_ending_here == max_so_far:
            start_old = start
            end = i
    Ret = [max_so_far, start_old, end]
    print("Elapsed time = %.3f ms" % ((time.time() - start_t) * 1000))
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
random.seed(1053578)
A = []
for i in range(10000):
    A.append(random.randint(-100, 100))
B = max_subarray(A)
print("The maximum sum is %d " % B[0])
print("The start index is %d " % B[1])
print("The end index is %d " % B[2])

