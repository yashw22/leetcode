class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # n = len(nums)
        # # picked = int(0)
        # curr = []

        # def dfs(picked):
        #     if len(curr) == n:
        #         res.append(curr.copy())
        #         return

        #     for i in range(n):
        #         if not (picked & (1<<i)):
        #             curr.append(nums[i])
        #             # picked |= 1<<i
        #             dfs(picked | (1<<i))
        #             curr.pop()
        #             # picked &= ~(1<<i)
                
        # dfs(0)
        # return res


        res = []
        curr = []
        visit = set()

        def rec():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in nums:
                if i not in visit:
                    curr.append(i)
                    visit.add(i)
                    rec()
                    visit.remove(i)
                    curr.pop()
            

        rec()
        return res