class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # itr = [[1,0],[0,-1],[-1,0],[0,1]]
        # m,n = len(heights), len(heights[0])

        # pac = [[False]*n for _ in range(m)]
        # atl = [[False]*n for _ in range(m)]

        # def bfs(src, visit):
        #     while src:
        #         r,c = src.popleft()
        #         visit[r][c]=True
        #         for i,j in itr:
        #             nr,nc = r+i,c+j
        #             if 0<=nr<m and 0<=nc<n and not visit[nr][nc] and heights[nr][nc]>=heights[r][c]:
        #                 src.append([nr,nc])
        
        # pacific,atlantic = deque(), deque()
        # for c in range(n):
        #     pacific.append([0,c])
        #     atlantic.append([m-1,c])
        # for r in range(m):
        #     pacific.append([r,0])
        #     atlantic.append([r,n-1])
        
        # bfs(pacific,pac)
        # bfs(atlantic,atl)

        # res =[]

        # for r in range(m):
        #     for c in range(n):
        #         if pac[r][c] and atl[r][c]:
        #             res.append([r,c])

        # return res

        m,n = len(heights), len(heights[0])
        pvisit = [[False]*n for _ in range(m)]
        avisit = [[False]*n for _ in range(m)]
        pacific, atlantic = deque(), deque()
        
        dir = [1,0,-1,0,1]
        def bfs(src, visit):
            while src:
                r, c = src.popleft()
                visit[r][c] = True
                
                for i in range(4):
                    nr, nc = r+dir[i], c+dir[i+1]
                    if 0<=nr<m and 0<=nc<n and not visit[nr][nc] and heights[nr][nc]>=heights[r][c]:
                        src.append((nr,nc))
        
        for c in range(n):
            pacific.append((0,c))
            atlantic.append((m-1,c))
        for r in range(m):
            pacific.append((r,0))
            atlantic.append((r,n-1))

        bfs(pacific, pvisit)
        bfs(atlantic, avisit)

        res = []
        for i in range(m):
            for j in range(n):
                if pvisit[i][j] and avisit[i][j]:
                    res.append([i,j])

        return res