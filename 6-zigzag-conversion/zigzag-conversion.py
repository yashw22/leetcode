class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<numRows: return s
        
        res = [[] for _ in range(numRows)]

        dir = 1
        curr = 0
        for c in s:
            res[curr].append(c)
            if curr==numRows-1:
                dir = -1
            if curr == 0:
                dir = 1
            curr += dir

        return "".join(["".join(row) for row in res])

        