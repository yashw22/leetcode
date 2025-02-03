class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        words = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }
        
        def getNumSet(curr):
            res = []

            if curr//100:
                res.append(words[curr//100])
                res.append("Hundred")

            curr %= 100
            if curr==0:
                pass
            elif curr<=20:
                res.append(words[curr])
            else:
                res.append(words[curr//10*10])
                if curr%10!=0: 
                    res.append(words[curr%10])

            return " ".join(res)


        res = []

        if num%1000!=0:
            res.append(getNumSet(num%1000))

        num = num//1000
        if num and num%1000!=0:
            res.append("Thousand")
            res.append(getNumSet(num%1000))
        
        num = num//1000
        if num and num%1000!=0:
            res.append("Million")
            res.append(getNumSet(num%1000))

        num = num//1000
        if num:
            res.append("Billion")
            res.append(getNumSet(num%1000))

        return " ".join(res[::-1])

        

