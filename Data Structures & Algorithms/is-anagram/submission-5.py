class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        for i in s:
            freq[i] =freq.get(i, 0) + 1
        for i in t:
            if i not in freq or freq[i] == 0:
                return False
            freq[i] = freq[i] - 1
        
        return True