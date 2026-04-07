from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        LeetCode 268 — Missing Number

        Approach (Bit Manipulation - XOR):
        - XOR all elements in the array
        - XOR all numbers from 0 to n
        - Pairs cancel out (a ^ a = 0)
        - Remaining value is the missing number

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        xor = 0
        n = len(nums)

        # XOR all numbers in the array
        for num in nums:
            xor ^= num

        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor ^= i

        return xor