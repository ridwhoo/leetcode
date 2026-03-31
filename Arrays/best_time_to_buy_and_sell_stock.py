"""
        LeetCode 121 — Best Time to Buy and Sell Stock

        Approach:
        - Track the minimum price seen so far
        - For each price, calculate potential profit
        - Update maximum profit accordingly

        Time Complexity: O(n)
        Space Complexity: O(1)
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]  
        max_profit = 0
        for price in prices :
            profit = price - min_price
            if profit > max_profit :
                max_profit = profit
            if price < min_price :
                min_price = price
        return max_profit                 