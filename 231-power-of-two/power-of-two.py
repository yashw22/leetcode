class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1: return True
        n = float(n)
        while n>1:
            print(n/2.0)
            if n/2.0 != int(n/2):
                return False
            n = n/2
        
        return True if n==1 else False
        