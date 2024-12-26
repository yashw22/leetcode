class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        even = [0]*n

        def bfs(node):
            if even[node]:
                return True

            q = deque([node])
            even[node] = 1

            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if not even[nei]:
                        q.append(nei)
                        even[nei] = -1 * even[curr]
                    elif even[curr]==even[nei]:
                        return False
            return True


        for i in range(n):
            if not bfs(i):
                return False
        return True