class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s = self.buildHashmap(s)
        hashmap_t = self.buildHashmap(t)
        return hashmap_s == hashmap_t
        

    def buildHashmap(self, s: str):
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        return hashmap