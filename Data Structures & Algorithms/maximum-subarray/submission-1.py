class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm n2 to n
        max_sum = nums[0]
        currsum = 0

        for num in nums:
            if currsum < 0:
                currsum = 0
            currsum += num
            max_sum = max(currsum, max_sum)  
        return max_sum      

        