class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1]*(n)

        # for i in range(n-2, -1, -1):
        #     for j in range(i, n):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1+dp[j])

        # return max(dp)

        n = len(nums)
        mem = [1]*n
        res = 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    mem[i] = max(mem[i], mem[j]+1)
                    if res < mem[i]:
                        res = mem[i]
                        continue
            
        return res



        