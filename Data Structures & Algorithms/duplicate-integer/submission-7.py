class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialize an empty hashset
        #iterate through each number in the array
        seen = set() 
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False             
        