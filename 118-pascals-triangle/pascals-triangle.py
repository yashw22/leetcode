class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]

        res = [[1], [1,1]]
        
        for row in range(2, numRows):
            level = [1]
            for i in range(1, row):
                level.append(res[-1][i-1] + res[-1][i])
            level.append(1)
            res.append(level)
        return res

        