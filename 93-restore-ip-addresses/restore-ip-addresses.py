class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        curr = []

        def isValid(num):
            if num=="" or int(num)>255 or (len(num)>1 and num[0]=="0"):
                return False
            return True

        def backtrack(idx, num):
            if idx==len(s):
                if len(curr)==4 and num=="":
                    res.append(".".join(curr))
                return
            if len(curr)==4 and not isValid(num):
                return

            num += s[idx]

            if isValid(num):
                curr.append(num)
                backtrack(idx+1, "")
                num = curr.pop()
                
            backtrack(idx+1, num)

        backtrack(0, "")
        return res