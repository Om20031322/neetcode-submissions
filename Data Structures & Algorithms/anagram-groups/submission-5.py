class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))

            if sorted_word not in groups:
                groups[sorted_word] = []

            groups[sorted_word].append(i)

        return list(groups.values())