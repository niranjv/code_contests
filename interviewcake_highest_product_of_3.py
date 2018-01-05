# URL: https://www.interviewcake.com/question/python/highest-product-of-3
# 
# Description:
# Given a list of integers, find the highest product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.
# 
# REQUIREMENTS:
# If list_of_ints is [-10, -10, 1, 3, 2], we should return 300 (which we get by taking -10 * -10 * 3).

def get_highest_product_sorting(nums):
    """
    :type nums: list of ints, with at least values

    Method:
    - Use sorting in O(N logN) time to get highest product of 3 numbers from the list

    Complexity: 
    - Time: O(N logN) since we sort input list 
    - Space: O(1) since we only store product
    """

    result_nums = []
    last_index = len(nums) - 1
    sorted_nums = sorted(nums, reverse=True) # This is O(N logN)

    # default result
    result = sorted_nums[0] * sorted_nums[1] * sorted_nums[2] 

    # handle case where 2 negatives at the end + 1 positive at the beginning of sorted list result in a higher product
    if sorted_nums[0] > 0 and -sorted_nums[last_index] > sorted_nums[1] and -sorted_nums[last_index-1] > sorted_nums[2]:
        result = sorted_nums[0] * sorted_nums[last_index] * sorted_nums[last_index - 1] 

    return result


def get_highest_product(nums):
    """
    Get result in O(n) time
    """
