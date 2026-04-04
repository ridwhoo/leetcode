from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        LeetCode 88 — Merge Sorted Array

        Approach:
        - Use three pointers starting from the end
        - Compare elements from nums1 and nums2
        - Place the larger element at the end of nums1
        - Continue until all elements of nums2 are placed

        Time Complexity: O(m + n)
        Space Complexity: O(1) (in-place)
        """

        # Pointer for last valid element in nums1
        p1 = m - 1

        # Pointer for last element in nums2
        p2 = n - 1

        # Pointer for position to fill in nums1
        write = m + n - 1

        # Merge from the back
        while p2 >= 0: 
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1

            write -= 1