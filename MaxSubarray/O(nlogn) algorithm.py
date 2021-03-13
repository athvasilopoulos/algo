"""
Maximum Sub-array Sum Problem
O(nlogn) Devide & Conquer algorithm
"""
import random
import time


def max_subarray(alist, start, end):
    if start == end - 1:
        return start, end, alist[start]
    else:
        mid = (start + end) // 2
        left_start, left_end, left_max = max_subarray(alist, start, mid)
        right_start, right_end, right_max = max_subarray(alist, mid, end)
        cross_start, cross_end, cross_max = find_max_crossing_subarray(
            alist, start, mid, end
        )
        if left_max > right_max and left_max > cross_max:
            return left_start, left_end, left_max
        elif right_max > left_max and right_max > cross_max:
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max


def find_max_crossing_subarray(alist, start, mid, end):
    sum_left = float("-inf")
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i
    sum_right = float("-inf")
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i
    return cross_start, cross_end, sum_left + sum_right


A = []
B = [0, 0, 0]
print("For the array with the 5000 elements:")
random.seed(1053578)
for i in range(5000):
    A.append(random.randint(-100, 100))
start_t = time.time()
B[1], B[2], B[0] = max_subarray(A, 0, 5000)
print("Elapsed time = %.3f ms" % ((time.time() - start_t) * 1000))
print("The maximum sum is %d " % B[0])
print("The start index is %d " % B[1])
print("The end index is %d " % B[2])
print("")

A = []
print("For the array with the 10000 elements:")
random.seed(1053578)
for i in range(10000):
    A.append(random.randint(-100, 100))
start_t = time.time()
B[1], B[2], B[0] = max_subarray(A, 0, 10000)
print("Elapsed time = %.3f ms" % ((time.time() - start_t) * 1000))
print("The maximum sum is %d " % B[0])
print("The start index is %d " % B[1])
print("The end index is %d " % B[2])
