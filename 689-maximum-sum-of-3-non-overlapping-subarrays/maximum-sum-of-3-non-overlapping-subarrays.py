class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        # -------------three pointer----------
        # n = len(nums)

        # currSum = sum(nums[:k])
        # sums = [currSum] + [0]*(n-1)

        # for i in range(k, n):
        #     currSum += nums[i] - nums[i-k]
        #     sums[i-k+1] = currSum

        # l_max, r_max = [0]*n, [n-k]*n
        # for i in range(k, n):
        #     if sums[i-k] > sums[l_max[i-1]]:
        #         l_max[i] = i-k
        #     else:
        #         l_max[i] = l_max[i-1]

        # for i in range(n-k-1, -1, -1):
        #     if sums[i] >= sums[r_max[i+1]]:
        #         r_max[i] = i
        #     else:
        #         r_max[i] = r_max[i+1]
            
        # # print(sums)
        # # print(l_max)
        # # print(r_max)

        # maxSum = sum(nums[:2*k])
        # res = [0,k, 2*k]
        # for i in range(k, n-2*k+1):
        #     currSum = sums[l_max[i]] + sums[i] + sums[r_max[i+k]]
        #     if currSum > maxSum:
        #         maxSum = currSum
        #         res = [l_max[i], i, r_max[i+k]]
        #     # print(l_max[i], i, r_max[i+k], currSum)
        
        # return res


        # ---------sliding window----------

        n = len(nums)

        lsum, msum, rsum = sum(nums[:k]), sum(nums[k:2*k]), sum(nums[2*k:3*k])
        lmaxsum, mmaxsum, rmaxsum = lsum, lsum+msum, lsum+msum+rsum
        lmaxidx, mmaxidx, rmaxidx = 0, [0,k], [0, k, 2*k]

        for i in range(1, n-3*k+1):
            a,b,c = i, i+k, i+2*k
            # print(i, a,b,c)
            # print(a-1,b-1,c-1)
            # print(a+k-1,b+k-1,c+k-1)
            lsum += nums[a+k-1]-nums[a-1]
            msum += nums[b+k-1]-nums[b-1]
            rsum += nums[c+k-1]-nums[c-1]

            if lsum>lmaxsum:
                lmaxsum = lsum
                lmaxidx = a

            currmsum = lmaxsum+msum
            if currmsum>mmaxsum:
                mmaxsum = currmsum
                mmaxidx = [lmaxidx, b]

            currrsum = mmaxsum+rsum
            if currrsum>rmaxsum:
                rmaxsum = currrsum
                rmaxidx = mmaxidx + [c]

        return rmaxidx