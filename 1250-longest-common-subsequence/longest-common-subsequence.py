class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # n1,n2 = len(text1), len(text2)
        # dp = [[0]*(n2+1) for _ in range(n1+1)]

        # for i in range(n1-1, -1, -1):
        #     for j in range(n2-1, -1, -1):
        #         if text1[i]==text2[j]:
        #             dp[i][j] = dp[i+1][j+1]+1
        #         else:
        #             dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        # return dp[0][0]

        n1, n2 = len(text1), len(text2)
        mem = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    mem[i][j] = mem[i-1][j-1]+1
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j-1])
                
        return mem[n1][n2]

