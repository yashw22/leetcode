class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # itr = [[0,1],[1,0],[0,-1],[-1,0]]
        # m, n = len(grid), len(grid[0])

        # def dfs(r, c):
        #     if grid[r][c]=="0":
        #         return

        #     grid[r][c]="0"
        #     for i,j in itr:
        #         x, y = r+i, c+j
        #         if -1<x<m and -1<y<n:
        #             dfs(x, y)

        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]=="1":
        #             res +=1
        #             dfs(i,j)
        
        # return res

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