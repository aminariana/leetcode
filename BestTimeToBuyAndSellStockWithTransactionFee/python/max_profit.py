from typing import List


def maxProfit(prices: List[int], fee: int) -> int:
    # e.g. prices [1,3,2,8,4,9], fee $2
    buy = prices[0]
    gain = 0
    for price in prices:
        # Suppose we sell at $8. Until we do, no gains.
        # So buy is $1 for [1, 3, 2, 8] window and gain is $5 after fees.
        buy = min(buy, price - gain)
        gain = max(gain, price - buy - fee)
        print(price, buy, gain)
        
        # In [4, 9] remaining window, the 4 can either be a buying point or a selling point.
        # However (by Dynamic Programming) the price 4 could append the DP solution either
        # as a selling point (bad) or as a buying point. If it's a buying point, it should
        # consider the discount of previous gains.

        # Effectively this is a 2xn DP array of buy and sell rows, optimizing to only
        # track the last column (2x1):

        # buy row  [[1, 1, 1, 1, -1, -1]     <--- buy price (4) is discounted by carried gain
        # gain row  [0, 0, 0, 5,  5,  8]]
    return gain
