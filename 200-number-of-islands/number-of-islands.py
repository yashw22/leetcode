class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # nxt = [0, 1, 0, -1, 0]
        # R, C = len(grid), len(grid[0])

        # def dfs(r,c):
        #     if r<0 or r>=R or c<0 or c>=C or grid[r][c]=="0":
        #         return
            
        #     grid[r][c] = "0"
        #     for i in range(4):
        #         dfs(r+nxt[i], c+nxt[i+1])

        # count = 0
        # for r in range(R):
        #     for c in range(C):
        #         if grid[r][c]=="1":
        #             count += 1
        #             dfs(r,c)

        # return count

        dir = [1,0,-1,0,1]
        def bfs(r,c):
            grid[r][c]="0"
            for i in range(4):
                nr, nc = r+dir[i], c+dir[i+1]
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]=="1":
                    bfs(nr,nc)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    bfs(i,j)
                    res += 1

        return res