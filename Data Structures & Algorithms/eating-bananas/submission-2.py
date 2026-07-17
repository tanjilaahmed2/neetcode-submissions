class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left<right:
            k = (left + right)//2
            totalhour = 0
            for pile in piles:
                totalhour += (math.ceil(pile/k))
            if totalhour <=h :
                right = k
            else: 
                left = k + 1 
       
        return right      



        