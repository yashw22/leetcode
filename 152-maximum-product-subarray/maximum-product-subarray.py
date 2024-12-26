class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]
        # cmin, cmax = 1, 1

        # for num in nums:
        #     tmp = cmax
        #     cmax = max(cmax*num, cmin*num, num)
        #     cmin = min(cmin*num,tmp*num, num)
        #     res = max(res,cmax)
        # return res

        cmax = cmin = 1
        res = nums[0]

        for num in nums:
            curr = cmax
            cmax = max(cmax*num, cmin*num, num)
            cmin = min(curr*num, cmin*num, num)
            res = max(res, cmax)

        return res


