from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        LeetCode 704 — Binary Search

        Approach:
        - Maintain search space [left, right]
        - Find mid and compare with target
        - Narrow search space accordingly

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            # Avoid potential overflow (important in some languages)
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1  # search right half

            else:
                right = mid - 1  # search left half

        return -1