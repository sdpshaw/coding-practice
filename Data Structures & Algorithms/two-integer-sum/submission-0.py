class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = dict()
        for i, val in enumerate(nums):
            diff = target - val
            if tmp.get(diff, None) is None:
                tmp[diff] = i
            if (tmp.get(val, None) is not None) and (tmp.get(val, None) != i):
                return [tmp.get(val, None), i]
