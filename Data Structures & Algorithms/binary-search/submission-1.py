class Solution:

    def binarySearch(self, l:int, r:int, nums:List[int], target: int)->int:
        m = l + (r -l)//2

        if l>r:
            return -1

        if target>nums[m]:   
            return self.binarySearch(m + 1, r, nums, target) 
        elif target<nums[m]:
            return self.binarySearch(l, m - 1, nums, target)   
        else:
            return m    


    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums)-1, nums, target)
        
                