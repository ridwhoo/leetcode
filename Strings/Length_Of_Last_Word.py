class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split()
        l = len(s1)
        return len(s1[-1])