class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            prod[i] = prefix
            prefix = nums[i]*prefix
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            prod[i]*= suffix    
            suffix = nums[i]*suffix
        return prod    
        