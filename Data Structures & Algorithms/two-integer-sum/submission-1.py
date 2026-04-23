class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in tmp:
                return [tmp[diff], i]
            tmp[val] = i
