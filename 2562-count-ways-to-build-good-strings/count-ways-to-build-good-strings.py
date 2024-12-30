class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [-1]*high
        mod = pow(10,9) + 7
        
        def rec(idx):
            if idx>high:
                return 0
            if idx==high:
                return 1
            if dp[idx] != -1:
                return dp[idx]

            count = 1 if idx>=low else 0

            count += rec(idx+zero)
            count %= mod
            
            count += rec(idx+one)
            count %= mod

            dp[idx] = count
            return count

        return rec(0)
        