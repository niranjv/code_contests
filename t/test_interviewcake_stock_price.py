import pytest
import interviewcake_stock_price # Module in parent dir found via $PYTHONPATH

def test_empty_list():

    with pytest.raises(Exception) as e:
        interviewcake_stock_price.get_max_profit([])
    assert str(e.value) == "Need at least 2 prices for stock"

def test_list_with_1_value():
    with pytest.raises(Exception) as e:
            interviewcake_stock_price.get_max_profit([1])
    assert str(e.value) == "Need at least 2 prices for stock"

def test_list_with_2_values():
    assert interviewcake_stock_price.get_max_profit([1,2]) == 1

def test_list_with_identical_values():
    assert interviewcake_stock_price.get_max_profit([1,1,1,1]) == 0

def test_list_with_non_monotonic_values():
    assert interviewcake_stock_price.get_max_profit([10, 7, 5, 8, 11, 9]) == 6

def test_list_with_increasing_values():
    assert interviewcake_stock_price.get_max_profit(range(1, 10)) == 8

def test_list_with_decreasing_values():
    assert interviewcake_stock_price.get_max_profit(range(20, 1, -2)) == -2
