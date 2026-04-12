from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        LeetCode 26 — Remove Duplicates from Sorted Array

        Approach (Two Pointers):
        - Use 'write' pointer to place next unique element
        - Traverse with 'read' pointer
        - When a new element is found, copy it to 'write' index

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Edge case: empty array
        if not nums:
            return 0

        write = 1  # position for next unique element

        # Traverse from second element
        for read in range(1, len(nums)):

            # If current element is different from previous
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write