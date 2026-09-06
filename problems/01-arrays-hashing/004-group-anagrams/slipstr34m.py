from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        
        for string_value in strs:
            hashed = tuple(sorted(list(string_value)))
            hash_map[hashed] = hash_map.get(hashed, [])
            hash_map[hashed].append(string_value)
        
        result = []
        for key, val in hash_map.items():
            result.append(val)

        return result