class Solution:
    def romanToInt(self, s: str) -> int:
        # res = 0
        # n=len(s)
       
        # for i in range(n):
        #     if s[i]=='I':
        #         if i!=n-1 and s[i+1] in ['V', 'X']:
        #             res -= 1
        #         else:
        #             res += 1
        #     elif s[i]=='V':
        #         res += 5
        #     elif s[i]=='X':
        #         if i!=n-1 and s[i+1] in ['L', 'C']:
        #             res -= 10
        #         else:
        #             res += 10
        #     elif s[i]=='L':
        #         res += 50
        #     elif s[i]=='C':
        #         if i!=n-1 and s[i+1] in ['D', 'M']:
        #             res -= 100
        #         else:
        #             res += 100
        #     elif s[i]=='D':
        #         res += 500
        #     elif s[i]=='M':
        #         res += 1000
            
        # return res

        romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # subtractMap = {'I': ['V', 'X'], 'X': ['L','C'], 'C': ['D', 'M']}

        res = 0
        n = len(s)
        for i in range(n):
            # if i!=n-1 and s[i] in subtractMap and s[i+1] in subtractMap[s[i]]:
            if i!=n-1 and romanMap[s[i+1]]>romanMap[s[i]]:
                res -= romanMap[s[i]]
            else:
                res += romanMap[s[i]]

        return res
