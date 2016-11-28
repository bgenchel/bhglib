"""
Given an array A = {a1, a2, ..., aN} of N elements, find the maximum possible 
sum of a Contiguous subarray or Non-contiguous (not necessarily contiguous) subarray.
Empty subarrays/subsequences should not be considered.
"""


def max_subarray(array):
    return max_contiguous_subarray(array), max_noncontiguous_subarray(array)


def max_contiguous_subarray(array):  # AKA Kudane's algorithm
    max_ending_here = max_so_far = array[0]
    for x in array[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


def max_noncontiguous_subarray(array):
    max_so_far = array[0]
    for x in array[1:]:
        max_so_far = max(x, max_so_far, max_so_far + x)
    return max_so_far

