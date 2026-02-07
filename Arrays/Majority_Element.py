# Approach 1: HashMap Approach
# Time: O(n), Space: O(n)

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for num in nums :
            if count == 0 :
                candidate = num
            if num == candidate :
                count += 1
            else :
                count -= 1
        return candidate            
    
# -----------------------------
# Approach 2: Dictionary Method
# Time: O(n), Space: O(n)
# -----------------------------
'''
class Solution:
    def majorityElement_dict(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for num in nums :
            d[num] = d.get(num, 0) + 1
        for k, v in d.items() :
            if v > n // 2 :
                return k
'''
