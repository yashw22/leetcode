class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        # n = len(x)
        # for i in range(floor(n/2)):
        #     if x[i]!=x[n-i-1]:
        #         return False
        return x==x[::-1]
        