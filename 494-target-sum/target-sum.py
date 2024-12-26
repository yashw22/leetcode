class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, tot):
            if i==len(nums):
                return 1 if tot==target else 0
            if (i, tot) in cache:
                return cache[(i,tot)]
            
            cache[(i,tot)] = dfs(i+1, tot+nums[i]) + dfs(i+1, tot-nums[i])
            return cache[(i,tot)]

        return dfs(0, 0)