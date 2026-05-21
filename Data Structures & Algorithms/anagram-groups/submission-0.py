class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            sorted_words = ''.join(sorted(word))
            if sorted_words not in freq:
                freq[sorted_words] = []
            
            freq[sorted_words].append(word)
        return list(freq.values())