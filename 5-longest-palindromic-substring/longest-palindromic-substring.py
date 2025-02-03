class Solution:
    def longestPalindrome(self, s: str) -> str:
        # n = len(s)
        # if n==1:
        #     return s

        # mx = 1
        # mi,mj = 0,0

        # def isPalin(x,y):
        #     while x<y:
        #         if s[x]!=s[y]:
        #             return False
        #         x+=1
        #         y-=1
        #     return True

        # for i in range(0, n-1):
        #     for j in range(i,n):
        #         if isPalin(i,j) and (j-i+1)>mx:
        #             mx = j-i+1
        #             mi,mj = i,j

        # return s[mi:mj+1]

        # res = ""
        # resLen = 0
        # for i in range(len(s)):
        #     l, r = i,i
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if (r-l+1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r-l+1
        #         l -=1
        #         r +=1

        #     l, r = i,i+1
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if (r-l+1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r-l+1
        #         l -=1
        #         r +=1

        # return res

        def getPalin(l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            return r-l+1-2, s[l+1: r]


        res = ""
        reslen = 0
        for i in range(len(s)):
            currlen, currPalin = getPalin(i, i)
            if currlen>reslen:
                reslen = currlen
                res = currPalin
            
            currlen, currPalin = getPalin(i, i+1)
            if currlen>reslen:
                reslen = currlen
                res = currPalin
            
        return res
