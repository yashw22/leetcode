class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        # print(s,g)

        gi = si = 0
        res = 0
        while gi<len(g) and si<len(s):
            # print(si, gi, s[si], g[gi])
            if s[si]>=g[gi]:
                res += 1
                si += 1
            gi += 1

        return res