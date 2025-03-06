class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = [1]
        curr = set()

        def dfs(idx, curr_str):
            if idx==len(s):
                if curr_str=="":
                    res[0] = max(res[0], len(curr))
                return

            dfs(idx+1, curr_str+s[idx])

            curr_str += s[idx]
            if curr_str not in curr:
                curr.add(curr_str)
                dfs(idx+1, "")
                curr.remove(curr_str)
            curr_str = curr_str[:-1]

        dfs(0, "")
        return res[0]