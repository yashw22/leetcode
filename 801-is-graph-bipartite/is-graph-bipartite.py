class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # -------bfs--------
        # n = len(graph)
        # even = [0]*n

        # def bfs(node):
        #     if even[node]:
        #         return True

        #     q = deque([node])
        #     even[node] = 1

        #     while q:
        #         curr = q.popleft()
        #         for nei in graph[curr]:
        #             if even[curr]==even[nei]:
        #                 return False
        #             elif not even[nei]:
        #                 q.append(nei)
        #                 even[nei] = -1 * even[curr]
        #     return True

        # for i in range(n):
        #     if not bfs(i):
        #         return False
        # return True

        # --------dfs---------
        n = len(graph)
        even = [0]*n

        def dfs(node, isEven):
            if even[node]:
                return True
            
            even[node] = 1 if isEven else -1

            for nei in graph[node]:
                if even[nei]==even[node] or not dfs(nei, not isEven):
                    return False
            return True
            
        
        for i in range(n):
            if not dfs(i, True):
                return False
        return True