from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        write = len(nums) - 1
        while left <= right :
            if abs(nums[left]) > abs(nums[right]) :
                result[write] = nums[left] * nums[left]
                write -= 1
                left += 1
            else :
                result[write] = nums[right] * nums[right]
                write -= 1
                right -= 1
        return result            