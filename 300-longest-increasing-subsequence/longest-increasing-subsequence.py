class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1]*(n)

        # for i in range(n-2, -1, -1):
        #     for j in range(i, n):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1+dp[j])

        # return max(dp)

        mem = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    mem[i] = max(mem[i], 1+mem[j])

        return max(mem)



        