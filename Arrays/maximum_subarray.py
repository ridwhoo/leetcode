from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        LeetCode 53 — Maximum Subarray

        Approach (Kadane’s Algorithm):
        - Maintain a running sum (curr_sum)
        - If curr_sum becomes negative, reset it to 0
        - Track the maximum sum seen so far

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        curr_sum = 0
        max_sum = nums[0]

        for num in nums:
            curr_sum += num

            # Update maximum subarray sum
            if curr_sum > max_sum:
                max_sum = curr_sum

            # Reset if current sum becomes negative
            if curr_sum < 0:
                curr_sum = 0

        return max_sum