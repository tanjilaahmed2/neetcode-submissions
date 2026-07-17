class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                return True
            else: 
                hashmap[i] = 1
                
        return False
sol = Solution()
nums = [1,2,3,3]   
res = sol.hasDuplicate(nums)             

         