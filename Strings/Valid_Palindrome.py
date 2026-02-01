class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        left = 0 ; right = len(s1) - 1
        while left < right :
            if not s1[left].isalnum() :
                left += 1
            elif not s1[right].isalnum() :
                right -= 1  
            else :
                if s1[left] != s1[right] :
                    return False
                else :
                    left += 1
                    right -= 1
        return True            