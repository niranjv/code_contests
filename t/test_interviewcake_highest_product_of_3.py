import pytest
import interviewcake_highest_product_of_3

def test_3_zeros():
    nums = [0,0,0]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == 0

def test_3_positives():

    nums = [4,5,6]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == 120

def test_positive_and_zero():

    nums = [7,8,0,9]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == 504

def test_negative_only():

    nums = [-4,-1,-3,-2]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == -6

def test_all_negative_and_zero():

    nums = [-4,-1,-3,-2,0]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == 0

def test_negative_and_positive_1():

    nums = [4,-1,-3,-2,0]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == 24

def test_negative_and_positive_2():

    nums = [7, 4, 2, -1, -20, -30]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == 4200

def test_sample_input():

    nums = [-10, -10, 1, 3, 2]
    result = interviewcake_highest_product_of_3.get_highest_product_sorting(nums)
    assert result == 300

