class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        sett = set()
        length = 0
        i = 0
        for j in range(len(s)):
            while s[j] in sett:
                sett.remove(s[i])
                i += 1
            sett.add(s[j])
            length = max(length,j-i+1)
        return length
            


        