class Solution:
    def intToRoman(self, num: int) -> str:

        romanMap = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }

        res = ""
        pos = 1
        while num!=0:
            curr = num%10
            num = num//10

            if curr==4:
                res += romanMap[5*pos]
                res += romanMap[pos]
            elif curr==9:
                res += romanMap[10*pos]
                res += romanMap[pos]
            elif curr>=5:
                res += romanMap[pos]*(curr-5) if curr!=5 else ""
                res += romanMap[5*pos]
            else:
                res += romanMap[pos]*curr


            pos *= 10

        
        return res[::-1]