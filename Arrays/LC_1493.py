from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        LeetCode 1493 — Longest Subarray of 1's After Deleting One Element

        Approach (Sliding Window):
        - Maintain a window with at most one zero
        - Expand right pointer
        - If zeros exceed 1, shrink from left
        - Window size (right - left) represents valid subarray length
          after deleting one element

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):

            # Count zeros in current window
            if nums[right] == 0:
                zero_count += 1

            # Shrink window if more than one zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update max length (delete one element → window size - 1)
            max_length = max(max_length, right - left)

        return max_length