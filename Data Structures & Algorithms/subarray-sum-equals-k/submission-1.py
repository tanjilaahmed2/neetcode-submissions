class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        prefixSum = {0:1}
        res = 0

        for num in nums:
            currsum += num
            diff = currsum - k

            if diff in prefixSum:
                res += prefixSum[diff]
            if currsum in prefixSum:
                prefixSum[currsum] += 1
            else:
                prefixSum[currsum] = 1    
        return res        




        