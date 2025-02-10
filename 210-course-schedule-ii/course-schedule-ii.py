class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indeg = [0]*numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indeg[u] += 1

        q = deque()
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        res = []

        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                res.append(curr)
                for nei in adj[curr]:
                    indeg[nei] -= 1
                    if indeg[nei]==0:
                        q.append(nei)

        return res if len(res)==numCourses else []
