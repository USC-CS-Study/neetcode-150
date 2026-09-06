class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_already = set()
        for num in nums:
            if num in seen_already:
                return True
            else:
                seen_already.add(num)
        return False