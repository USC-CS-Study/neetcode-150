class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        others_need = {}
        for i, num in enumerate(nums):
            if num in others_need:
                return [others_need[num], i]
            else:
                others_need[target-num] = i 