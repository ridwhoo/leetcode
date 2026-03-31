from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        LeetCode 217 — Contains Duplicate

        Approach:
        - Use a hashmap (dictionary) to store frequency of elements
        - If any element appears more than once, return True immediately

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Dictionary to store frequency of elements
        freq = {}

        # Traverse through the array
        for num in nums:
            # Update frequency count
            freq[num] = freq.get(num, 0) + 1

            # If duplicate found, return True
            if freq[num] > 1:
                return True

        # No duplicates found
        return False