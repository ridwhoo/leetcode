class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_freq = {}
        for ch in magazine :
            mag_freq[ch] = mag_freq.get(ch, 0) + 1
        for ch in ransomNote :
            if ch not in mag_freq or mag_freq[ch] == 0 :
                return False
            mag_freq[ch] -= 1
        return True            