class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            newsubsets = []
            for subset in res:
                newsubsets.append(subset + [num])
            res.extend(newsubsets)
        return res        