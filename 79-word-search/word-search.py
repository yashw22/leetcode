class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [1,0,-1,0,1]
        visit = set()

        def dfs(r,c, idx):
            if idx == len(word):
                return True
            
            visit.add((r,c))
            for i in range(4):
                nr, nc = r+dir[i], c+dir[i+1]
                if 0<=nr<len(board) and 0<=nc<len(board[0]) and (nr,nc) not in visit and board[nr][nc] == word[idx] and dfs(nr,nc, idx+1):
                    return True
            visit.remove((r,c))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and dfs(i,j,1):
                    return True
        return False