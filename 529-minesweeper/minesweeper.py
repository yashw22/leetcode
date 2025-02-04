class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        visited = set()

        def getNeighbors(r,c):
            neiList = []
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if (i==0 and j==0) or r+i<0 or c+j<0 or r+i>=m or c+j>=n:
                        continue
                    neiList.append((r+i,c+j))

            return neiList

        def revealNieghbors(r,c):
            visited.add((r,c))
            neiMines = getNeighborMines(r,c)
            if neiMines > 0:
                board[r][c] = str(neiMines)
                return
            
            board[r][c] = "B"
            for nr, nc in getNeighbors(r,c):
                if (nr, nc) in visited or board[nr][nc]!="E":
                    continue
                revealNieghbors(nr,nc)
        
        def getNeighborMines(r,c):
            count = 0
            for nr, nc in getNeighbors(r,c):
                if board[nr][nc]=="M":
                    count += 1
            return count

        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        revealNieghbors(click[0], click[1])
        return board
