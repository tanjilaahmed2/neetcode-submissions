#from typing import List
#from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            output = [0]*26
            for char in s:
                output[ord(char) - ord('a')] += 1
            key = tuple(output) 
            hashmap[key].append(s)
        return list(hashmap.values())       

      