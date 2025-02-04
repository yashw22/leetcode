class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parenMap = {'(': ')', '{': '}', '[':']'}

        for ch in s:
            if ch in parenMap:
                stack.append(ch)
            elif len(stack)==0 or parenMap[stack[-1]]!=ch:
                return False
            else:
                stack.pop()

        return len(stack)==0


        