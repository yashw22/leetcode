class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0-0 
        # 0-1 2
        # 1-0 3
        # 1-1 
        m, n = len(board), len(board[0])

        def getLiveNei(r, c):
            count = 0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if (i==0 and j==0) or r+i<0 or c+j<0 or r+i>=m or c+j>=n:
                        continue
                    if board[r+i][c+j] in [1,3]:
                        count +=1

            return count
        
        for i in range(m):
            for j in range(n):
                live = getLiveNei(i,j)
                if board[i][j]==0:
                    if live==3:
                        board[i][j] = 2
                else:
                    if live<2:
                        board[i][j] = 3
                    elif live>3:
                        board[i][j] = 3
    
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j] = 1
                elif board[i][j]==3:
                    board[i][j] = 0