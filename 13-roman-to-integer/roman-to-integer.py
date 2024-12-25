class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n=len(s)
       
        for i in range(n):
            if s[i]=='I':
                if i!=n-1 and s[i+1] in ['V', 'X']:
                    res -= 1
                else:
                    res += 1
            elif s[i]=='V':
                res += 5
            elif s[i]=='X':
                if i!=n-1 and s[i+1] in ['L', 'C']:
                    res -= 10
                else:
                    res += 10
            elif s[i]=='L':
                res += 50
            elif s[i]=='C':
                if i!=n-1 and s[i+1] in ['D', 'M']:
                    res -= 100
                else:
                    res += 100
            elif s[i]=='D':
                res += 500
            elif s[i]=='M':
                res += 1000
            
        return res