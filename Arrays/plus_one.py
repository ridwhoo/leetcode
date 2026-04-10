from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        LeetCode 66 — Plus One

        Approach:
        - Traverse digits from right to left
        - If digit < 9 → increment and return
        - If digit == 9 → set to 0 and carry over
        - If all digits are 9 → prepend 1

        Time Complexity: O(n)
        Space Complexity: O(1) (ignoring output)
        """

        # Traverse from last digit to first
        for i in range(len(digits) - 1, -1, -1):

            # If current digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If digit is 9, set to 0 and continue (carry)
            digits[i] = 0

        # If all digits were 9 (e.g., 999 → 1000)
        return [1] + digits