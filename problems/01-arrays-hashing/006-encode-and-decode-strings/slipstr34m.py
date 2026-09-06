from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += i + "<break>"
        return encoded 

    def decode(self, s: str) -> List[str]:
        return s.split("<break>")[:-1]