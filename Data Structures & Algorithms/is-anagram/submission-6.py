class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {} #hashmap

        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for j in t:
            if j in seen:
                seen[j] -= 1
            else:
                return False
        for k in seen:
            if seen[k] != 0:
                return False
            
        return True


                

      
        