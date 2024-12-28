class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        currSum = sum(nums[:k])
        sums = [currSum] + [0]*(n-1)

        for i in range(k, n):
            currSum += nums[i] - nums[i-k]
            sums[i-k+1] = currSum

        l_max, r_max = [0]*n, [n-k]*n
        for i in range(k, n):
            if sums[i-k] > sums[l_max[i-1]]:
                l_max[i] = i-k
            else:
                l_max[i] = l_max[i-1]

        # for i in range(n-1, n-k-1, -1): r_max[i]=n-k
        for i in range(n-k-1, -1, -1):
            # print(i)
            if sums[i] >= sums[r_max[i+1]]:
                r_max[i] = i
            else:
                r_max[i] = r_max[i+1]
            
        # print(sums)
        # print(l_max)
        # print(r_max)

        maxSum = sum(nums[:2*k])
        res = [0,k, 2*k]
        for i in range(k, n-2*k+1):
            currSum = sums[l_max[i]] + sums[i] + sums[r_max[i+k]]
            if currSum > maxSum:
                maxSum = currSum
                res = [l_max[i], i, r_max[i+k]]
            # print(i, ":", l_max[i], r_max[i+k], currSum)

        


        return res