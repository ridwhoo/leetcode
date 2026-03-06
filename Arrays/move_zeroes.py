# LeetCode 283 — Move Zeroes
# Approach: Two Pointer (In-place swap)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)) :
            if nums[fast] != 0 :
                nums[fast] , nums[slow] = nums[slow] , nums[fast]
                slow += 1


