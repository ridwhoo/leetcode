from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        LeetCode 448 — Find All Numbers Disappeared in an Array

        Approach:
        - Use index marking technique (in-place)
        - For each number n, mark index (n - 1) as negative
        - Indices with positive values represent missing numbers

        Time Complexity: O(n)
        Space Complexity: O(1) (excluding output list)
        """

        # Mark indices corresponding to values as visited
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        result = []

        # Collect indices that remain positive (numbers that are missing)
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)

        return result