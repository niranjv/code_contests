# URL: https://www.interviewcake.com/question/python/stock-price
#
# Description:
# Write an efficient function that takes a list of prices for a stock and returns the best profit that could have made from 1 purchase and 1 sale of the stock yesterday.
# 
# For example:

# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# get_max_profit(stock_prices_yesterday)
# # returns 6 (buying for $5 and selling for $11)
# 
# REQUIREMENTS:
# - Stock price list index is time => stock prices are in ascending order of time
# - No "shorting" — you must buy before you sell. 
# - You may not buy and sell in the same time step (at least 1 minute must pass).


def get_max_profit(stock_prices):
    """
    :type stock_prices: list of real numbers representing price of a stock at a given minute in USD
    Complexity: O(n) time; O(1) space
    """

    if len(stock_prices) < 2: raise Exception("Need at least 2 prices for stock")

    min_price = stock_prices[0]
    max_profit = None

    for i in range(1, len(stock_prices)):

            cur_price = stock_prices[i]
            cur_profit = cur_price - min_price 

            if max_profit is None or cur_profit > max_profit:
                max_profit = cur_profit

            min_price = min(min_price, cur_price)

    return max_profit
