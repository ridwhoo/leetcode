from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        LeetCode 27 — Remove Element

        Approach (Two Pointers - Swap with End):
        - Use 'i' to scan from left
        - Use 'last' to track end of valid elements
        - If nums[i] == val → swap with last and shrink window
        - Else → move forward

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        i = 0
        last = len(nums) - 1

        while i <= last:
            if nums[i] == val:
                # Replace current element with last valid element
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1  # shrink valid range
            else:
                i += 1  # move forward only if current is valid

        return last + 1