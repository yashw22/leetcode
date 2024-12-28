class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for s,e in intervals[1:]:
            ls, le = res[-1]
            if s <= le:
                res[-1][1] = max(le, e)
            else:
                res.append([s,e])

        return res