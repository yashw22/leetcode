class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        targetlen = len(target)
        wordlen = len(words[0])
        arrlen = len(words)
        mod = pow(10, 9) + 7

        dp = {}

        f = [{} for _ in range(wordlen)]

        for word in words:
            for i, ch in enumerate(word):
                if ch in f[i]:
                    f[i][ch] += 1
                else:
                    f[i][ch] = 1


        # def rec(targetidx, kidx):
        #     if targetidx==targetlen:
        #         return 1
        #     if kidx==wordlen:
        #         return 0
        #     if (targetidx, kidx) in dp:
        #         return dp[(targetidx, kidx)]
            
        #     count = 0
        #     for word in words:
        #         if word[kidx]==target[targetidx]:
        #             count += rec(targetidx+1, kidx+1)
        #             count %= mod

        #     count += rec(targetidx, kidx+1)
        #     count %= mod

        #     dp[(targetidx, kidx)] = count
        #     return count

        def rec(targetidx, kidx):
            if targetidx==targetlen:
                return 1
            if kidx==wordlen:
                return 0
            if (targetidx, kidx) in dp:
                return dp[(targetidx, kidx)]
            
            count = 0
            if target[targetidx] in f[kidx]:
                count += f[kidx][target[targetidx]]*rec(targetidx+1, kidx+1)
                count %= mod
            
            count += rec(targetidx, kidx+1)
            count %= mod

            dp[(targetidx, kidx)] = count
            return count

        return rec(0,0)