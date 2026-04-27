# The isBadVersion API is provided by LeetCode.
# def isBadVersion(version: int) -> bool:

# mock function for local testing
bad = 4

def isBadVersion(version):
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        LeetCode 278 — First Bad Version

        Approach (Binary Search on Answer):
        - Search space: [1, n]
        - If mid is bad → answer is in left half (including mid)
        - If mid is good → answer is in right half
        - Continue until left == right

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        left, right = 1, n

        while left < right:
            # Safer mid calculation
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # mid could be the first bad → keep it
                right = mid
            else:
                # mid is good → discard left half
                left = mid + 1

        # left == right → first bad version
        return left