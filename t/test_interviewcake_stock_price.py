import pytest
import interviewcake_stock_price

def test_get_max_profit():

    assert interviewcake_stock_price.get_max_profit([1,2]) == 1
    assert interviewcake_stock_price.get_max_profit([1,1,1,1]) == 0
    assert interviewcake_stock_price.get_max_profit([10, 7, 5, 8, 11, 9]) == 6
    assert interviewcake_stock_price.get_max_profit(range(1, 10)) == 8
    assert interviewcake_stock_price.get_max_profit(range(20, 1, -2)) == -2

    # verify invalid input causes function to fail
    with pytest.raises(Exception) as e:
        interviewcake_stock_price.get_max_profit([])
    assert str(e.value) == "Need at least 2 prices for stock"

    with pytest.raises(Exception) as e:
        interviewcake_stock_price.get_max_profit([1])
    assert str(e.value) == "Need at least 2 prices for stock"
