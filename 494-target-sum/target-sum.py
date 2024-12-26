class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # cache = {}

        # def dfs(i, tot):
        #     if i==len(nums):
        #         return 1 if tot==target else 0
        #     if (i, tot) in cache:
        #         return cache[(i,tot)]
            
        #     cache[(i,tot)] = dfs(i+1, tot+nums[i]) + dfs(i+1, tot-nums[i])
        #     return cache[(i,tot)]

        # return dfs(0, 0)

        n = len(nums)
        mem = {}
        
        def dfs(i, curr):
            if i==n:
                return 1 if curr==target else 0

            if (i,curr) in mem:
                return mem[(i,curr)]

            mem[(i,curr)] = dfs(i+1, curr+nums[i]) + dfs(i+1, curr-nums[i])
            return mem[(i,curr)]

        return dfs(0,0)

                

        


