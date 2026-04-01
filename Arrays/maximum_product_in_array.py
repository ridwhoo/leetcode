from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        LeetCode 1464 — Maximum Product of Two Elements in an Array

        Approach:
        - Find the two largest numbers in a single pass
        - Compute (max1 - 1) * (max2 - 1)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Initialize two largest values
        max1 = float('-inf')
        max2 = float('-inf')

        # Traverse the array to find top two maximum values
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        # Calculate final product
        return (max1 - 1) * (max2 - 1)