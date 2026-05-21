class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        if len(setnums) == len(nums):
            return False
        else:
            return True