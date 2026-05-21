class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, val in enumerate(nums):
            compliment = target - val
            if compliment in res:
                return [res[compliment],i]
            
            res[val] = i