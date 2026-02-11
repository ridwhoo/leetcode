from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i= 1; unique_index = 1 
        while i < len(nums) :
            if nums[i] == nums[i-1] :
                i += 1
            else : 
                nums[unique_index] = nums[i]
                i += 1
                unique_index += 1
        return unique_index
