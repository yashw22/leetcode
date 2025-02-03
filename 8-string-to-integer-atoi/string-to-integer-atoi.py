class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i = 0

        while i<len(s) and s[i]==" ":
            i += 1
        if i==len(s):
            return 0

        if s[i] in "-+":
            if s[i]=="-":
                sign = -1
            i += 1

        while i<len(s) and s[i]=="0":
            i += 1
        
        while True:
            if i<len(s) and s[i] in "1234567890":
                # print(i, s[i])
                res *= 10
                res += int(s[i])
                i += 1
            else:
                res *= sign
                if res > pow(2, 31)-1:
                    return pow(2, 31)-1
                elif res < -pow(2,31):
                    return -pow(2,31)
                else:
                    return res

            
