import pytest
import interviewcake_product_of_other_numbers # Module in parent dir found via $PYTHONPATH

def test_empty_array():
    nums = []
    with pytest.raises(Exception) as e:
        result = interviewcake_product_of_other_numbers.get_products_of_all_ints_except_at_index(nums)
    assert str(e.value) == "Need at least 2 numbers in the input array" 

def test_array_with_1_number():
    nums = [1]
    with pytest.raises(Exception) as e:
        result = interviewcake_product_of_other_numbers.get_products_of_all_ints_except_at_index(nums)
    assert str(e.value) == "Need at least 2 numbers in the input array"

def test_array_with_2_numbers():
    nums = [1, 2]
    result = interviewcake_product_of_other_numbers.get_products_of_all_ints_except_at_index(nums)
    assert result == [2, 1]

def test_array_with_3_numbers():
    nums = [4, 5, 6]
    result = interviewcake_product_of_other_numbers.get_products_of_all_ints_except_at_index(nums)
    assert result == [30, 24, 20]

def test_sample_array_with_zeros():
    # test sample input array in problem description
    nums = [1, 2, 0, 4]
    result = interviewcake_product_of_other_numbers.get_products_of_all_ints_except_at_index(nums)
    assert result == [0, 0, 8, 0]

def test_sample_array_1():
    # test sample input array in problem description
    nums = [1, 7, 3, 4]
    result = interviewcake_product_of_other_numbers.get_products_of_all_ints_except_at_index(nums)
    assert result == [84, 12, 28, 21]

def test_sample_array_2():
    # test sample input array in problem description
    nums = [1, 2, 6, 5, 9]
    result = interviewcake_product_of_other_numbers.get_products_of_all_ints_except_at_index(nums)
    assert result == [540, 270, 90, 108, 60]
