# LeetCode 283 — Move Zeroes
# Approach: Two Pointer (In-place swap)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr_index = 0
        non_zero_index = 0
        for i in range(len(nums)) :
            if nums[i] != 0 :
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1
