class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictval = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in dictval:
                return[dictval[complement], i]

            dictval[val] = i

        