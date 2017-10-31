# URL: https://www.interviewcake.com/question/python/which-appears-twice
# 
# Description:
# I have a list of n + 1 numbers. Every number in the range 1..n appears once except for one number that appears twice.
# 
# Write a function for finding the number that appears twice.
# 
# REQUIREMENTS:
# - Do this with O(1) additional memory


def find_repeat(nums):
    """
    :type nums: list of ints

    Method:
    - Sort list and check for pair of repeated numbers
    - Will work for floats also if same precision is assumed for both copies of the number

    Complexity:
    - Time: O(N logN) to sort list
    - Space: O(N) since we need to store the sorted list in addition to the original list

    """

    n = len(nums)
    if n < 2: raise ValueError("Input must contain at least 2 numbers")

    sorted_nums = sorted(nums)
    print(sorted_nums)

    for i in range(n):
        if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
            return sorted_nums[i]


def find_repeat_2(nums):
    """
    :type nums: list of ints - list of integers from 1 .. n with 1 number in this interval present twice

    Method:
    - Calculate sum of first n numbers as n(n+1)/2. Subtract from sum of input list to get the number that is repeated.
    - For large n, this method can result in integer overflow in languages like C/C++. This cannot happen in Python 3 since ints can represent integers with arbitrary precision.

    Complexity:
    - Time: O(n) to sum all numbers in the input list
    - Space: O(1) to store values for 2 sums
    """

    n = len(nums)
    if n < 2: raise ValueError("Input must contain at least 2 numbers")

    first_n_sum = (n-1)*n/2
    list_sum = sum(nums)
    repeated_number = list_sum - first_n_sum

    return repeated_number

