class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev = [[] for _ in range(n)]
        for i, u in enumerate(graph):
            for v in u:
                rev[v].append(i)
        # print(rev)

        indeg = [0]*n
        for u in rev:
            for v in u:
                indeg[v] += 1

        # print(indeg) 

        res = []
        q = deque()
        for i in range(n):
            if indeg[i]==0:
                q.append(i)

        visited = [False]*n
        while q:
            node = q.pop()
            res.append(node)
            visited[node]=True
            for curr in rev[node]:
                if not visited[curr]:
                    indeg[curr] -= 1
                    if indeg[curr]==0:
                        q.append(curr)

        return sorted(res)