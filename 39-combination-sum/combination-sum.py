class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # curr = []

        # def rec(idx, s):
        #     if s>target or idx==len(candidates):
        #         return
        #     if s==target:
        #         res.append(curr.copy())
        #         return
            
        #     curr.append(candidates[idx])
        #     rec(idx, s+candidates[idx])
        #     curr.pop()

        #     rec(idx+1, s)

        # rec(0, 0)
        # return res

        res = []
        curr = []

        def rec(idx, s):
            if s>target or idx==len(candidates):
                return
            if s==target:
                res.append(curr[:])
                return
            
            curr.append(candidates[idx])
            rec(idx, s+candidates[idx])
            curr.pop()

            rec(idx+1, s)

        rec(0, 0)
        return res