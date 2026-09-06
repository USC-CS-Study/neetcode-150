from typing import List
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0)
            hash_map[nums[i]] += 1
        
        heap = []
        
        for key, val in hash_map.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)
        
        result = []
        for _ in range(k):
            result.append(heappop(heap)[1])
        
        return result