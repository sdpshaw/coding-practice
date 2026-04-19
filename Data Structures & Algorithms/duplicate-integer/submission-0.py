class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set(nums)
        if len(nums) == len(l):
            return False
        return True