class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if m!=n:
            return False

        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in t:
            if char not in hashmap:
                return False 
            else: 
                hashmap[char] -= 1

        for value in hashmap.values():
            if value != 0:
                return False
        return True               



        