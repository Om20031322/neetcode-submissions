class Solution:
    def encode(self, strs: List[str]) -> str:
        enc = ""
        for i in strs:
            length = len(i)
            enc = enc + str(length) + "#" + i
        return enc
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while  s[j] != '#':
                j = j + 1
            length = int(s[i:j])
            j = j+1
            word = s[j:j+length]
            result.append(word)
            i = j + length
        return result


