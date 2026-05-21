class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in dicts:
                dicts[ch] = dicts[ch] + 1
            else:
                dicts[ch] = 1
        
        for ch in t:
            if ch not in dicts:
                return False
            
            dicts[ch] = dicts[ch] - 1

        for value in dicts.values():
            if value != 0:
                return False

        return True
