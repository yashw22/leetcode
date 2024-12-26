class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # n1,n2 = len(word1), len(word2)

        # mem = {}
        # def dfs(i,j):
        #     if i==n1 and j==n2:
        #         return 0
        #     if i==n1 or j==n2:
        #         return max(n1-i, n2-j)
        #     if (i,j) in mem:
        #         return mem[(i,j)]

        #     tmp = float("inf")
        #     if word1[i]==word2[j]:
        #         tmp = min(tmp, dfs(i+1,j+1))
        #     else:
        #         tmp2 = min(dfs(i+1,j), dfs(i,j+1), dfs(i+1, j+1)) + 1
        #         tmp = min(tmp, tmp2)
        #     mem[(i,j)] = tmp
        #     return tmp
        
        # return dfs(0,0)

        # n1,n2 = len(word1), len(word2)

        # mem = [ [float("inf")]*(n2+1) for _ in range(n1+1)]
        # for j in range(n2+1):
        #     mem[n1][j] = n2-j
        # for i in range(n1+1):
        #     mem[i][n2] = n1-i

        # for i in range(n1-1, -1, -1):
        #     for j in range(n2-1, -1, -1):
        #         if word1[i]==word2[j]:
        #             mem[i][j] = mem[i+1][j+1]
        #         else:
        #             mem[i][j] = min(mem[i][j+1], mem[i+1][j], mem[i+1][j+1])+1

        # return mem[0][0]

        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(n1+1): dp[i][0]=i
        for i in range(n2+1): dp[0][i]=i

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[n1][n2]





            
            
        

        