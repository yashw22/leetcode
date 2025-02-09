class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mem = grid[:][:]

        for r in range(1,m):
            mem[r][0] += mem[r-1][0]
        for c in range(1,n):
            mem[0][c] += mem[0][c-1]

        for i in range(1, m):
            for j in range(1, n):
                mem[i][j] += min(mem[i-1][j], mem[i][j-1])

        return mem[-1][-1]