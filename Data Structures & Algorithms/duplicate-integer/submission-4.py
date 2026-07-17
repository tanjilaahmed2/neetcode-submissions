class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap
        #iterative
        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
    
            else:
                return True   
        return False        



        