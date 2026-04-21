from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        LeetCode 414 — Third Maximum Number

        Approach:
        - Track top three distinct maximum values
        - Skip duplicates
        - Update first, second, third accordingly

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        first = second = third = float('-inf')

        for num in nums:

            # Skip duplicates
            if num == first or num == second or num == third:
                continue

            # Update top three values
            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

        # If third max doesn't exist, return max
        return third if third != float('-inf') else first