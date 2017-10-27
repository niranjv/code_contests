# URL: https://www.interviewcake.com/question/python/product-of-other-numbers
# 
# Description:
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
# For example, given:
# 
#   [1, 7, 3, 4]
# 
# your function would return:
# 
# [84, 12, 28, 21]
# 
# by calculating:
#
# [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

from operator import mul
from functools import reduce

def get_products_of_all_ints_except_at_index(nums):
    """
    As we loop through array, calculate before_product from both ends in the same iteration to get O(n) time complexity
    Complexity: O(n) time (to loop thru array ONCE & make 4 multiplications per iteration); O(n) space (for final list of products)
    """

    n = len(nums) 
    last_index = n - 1
    if n < 2: raise Exception("Need at least 2 numbers in the input array")

    result = [None] * n
    before_prod = reverse_before_prod = 1
    result[0] = 1 # to be multiplied by after_prod in loop

    for i in range(n):

        # Calculate before_product in the forward direction
        # i = 0 => before_prod = 1
        if i > 0:
            before_prod = before_prod * nums[i-1]

        if result[i] is None:
            result[i] = before_prod
        else:
            result[i] = result[i] * before_prod
        
        # Calculate before_product in the reverse direction
        # i == n-1 => reverse_before_prod = 1
        if (n-i-1) == last_index:
            reverse_before_prod = 1
        if (n-i-1) < last_index:
            reverse_before_prod = reverse_before_prod * nums[n-i]

        if result[last_index-i] is None:
            result[last_index-i] = reverse_before_prod
        else:
            result[last_index-i] = result[last_index-i] * reverse_before_prod

    return result
