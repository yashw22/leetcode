class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for s,e in intervals[1:]:
            sl, el = res[-1]

            if el<s:
                res.append([s,e])
            else:
                res[-1][1] = max(e, el)

        return res