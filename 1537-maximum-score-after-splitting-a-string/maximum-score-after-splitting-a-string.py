class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        l = [0]*(n-1)
        r = [0]*(n-1)

        curr = 0
        for i in range(n-1):
            curr += 1 if s[i]=='0' else 0
            l[i] = curr

        curr = 0
        for i in range(n-1, 0, -1):
            curr += 1 if s[i]=='1' else 0
            r[i-1] = curr

        # print(l, r)
        res = 0
        for i in range(n-1):
            res = max(res, l[i]+r[i])
        
        return res