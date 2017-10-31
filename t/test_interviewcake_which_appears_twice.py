import pytest
import interviewcake_which_appears_twice # Module in parent dir found via $PYTHONPATH

def test_empty_list():
    nums=[]
    with pytest.raises(Exception) as e:
        interviewcake_which_appears_twice.find_repeat_2(nums)
    assert str(e.value) == "Input must contain at least 2 numbers"

def test_list_with_1_number():
    nums=[1]
    with pytest.raises(Exception) as e:
        interviewcake_which_appears_twice.find_repeat_2(nums)
    assert str(e.value) == "Input must contain at least 2 numbers"

def test_list_with_3_numbers():
    nums=[1,2,2]
    result = interviewcake_which_appears_twice.find_repeat_2(nums)
    assert result == 2

def test_list_with_11_numbers():
    nums = list(range(1,11))
    nums.append(5)
    result = interviewcake_which_appears_twice.find_repeat_2(nums)
    assert result == 5

def test_list_with_1001_numbers():
    nums = list(range(1,1001))
    nums.append(1)
    result = interviewcake_which_appears_twice.find_repeat_2(nums)
    assert result == 1
