# LeetCode 283 — Move Zeroes

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Approach: Two Pointers (In-place swap)

        - Use 'slow' pointer to track position for next non-zero element
        - Traverse array with 'fast' pointer
        - Swap when a non-zero element is found

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        slow = 0  # Position to place next non-zero element

        # Traverse array
        for fast in range(len(nums)):

            # If current element is non-zero, swap with 'slow'
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1  # Move slow pointer forward