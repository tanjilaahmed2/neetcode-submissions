# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        #length of the list
        n = len(pairs)
        res = [] # intermediate states

        for i in range(n): #i will track the current position
            j = i -1 # j will track the one position before current

            while j>= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -=1
            res.append(pairs[:])
        return res    




