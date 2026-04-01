from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        LeetCode 349 — Intersection of Two Arrays

        Approach:
        - Convert nums1 into a set for O(1) lookup
        - Iterate through nums2 and collect common elements in a result set
        - Use a set to ensure uniqueness

        Time Complexity: O(n + m)
        Space Complexity: O(n)
        """

        # Convert nums1 to set for fast lookup
        set1 = set(nums1)

        # Set to store unique intersection elements
        result = set()

        # Traverse nums2 and check for common elements
        for num in nums2:
            if num in set1:
                result.add(num)

        # Convert result set to list before returning
        return list(result)
    
    #Cleaner Pythonic Version 
    #return list(set(nums1) & set(nums2))