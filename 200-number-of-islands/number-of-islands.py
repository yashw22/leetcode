class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nxt = [0, 1, 0, -1, 0]
        R, C = len(grid), len(grid[0])

        def dfs(r,c):
            if r<0 or r>=R or c<0 or c>=C or grid[r][c]=="0":
                return
            
            grid[r][c] = "0"
            for i in range(4):
                dfs(r+nxt[i], c+nxt[i+1])

        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1":
                    count += 1
                    dfs(r,c)

        return count