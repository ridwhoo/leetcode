class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split()  
        lst = []  
        for word in s1 :
            w = word[::-1]
            lst.append(w)
        result = " ".join(lst)
        return result