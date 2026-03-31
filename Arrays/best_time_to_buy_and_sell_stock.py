from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        LeetCode 121 — Best Time to Buy and Sell Stock

        Approach:
        - Track the minimum price seen so far
        - For each price, calculate potential profit
        - Update maximum profit accordingly

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Initialize minimum price as the first day's price
        min_price = prices[0]

        # Initialize maximum profit to 0 (no profit initially)
        max_profit = 0

        # Traverse through prices
        for price in prices:
            # Calculate profit if sold today
            profit = price - min_price

            # Update maximum profit if current profit is higher
            if profit > max_profit:
                max_profit = profit

            # Update minimum price if current price is lower
            if price < min_price:
                min_price = price

        return max_profit