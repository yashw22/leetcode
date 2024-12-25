class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        e1 = {}
        for u,v in edges1:
            if u in e1: e1[u].append(v)
            else: e1[u] = [v]
            if v in e1: e1[v].append(u)
            else: e1[v] = [u]
        
        e2 = {}
        for u,v in edges2:
            if u in e2: e2[u].append(v)
            else: e2[u] = [v]
            if v in e2: e2[v].append(u)
            else: e2[v] = [u]
            

        def findDiameter(graph):
            if not graph.keys():
                return 0
            
            q = deque([0])
            visited = set()

            last = 0
            while q:
                n = len(q)

                for _ in range(n):
                    curr = q.popleft()
                    visited.add(curr)
                    last = curr
                    for nei in graph[curr]:
                        if nei not in visited:
                            q.append(nei)

            q = deque([last])
            visited = set()

            diameter = -1
            while q:
                n = len(q)
                diameter += 1

                for _ in range(n):
                    curr = q.popleft()
                    visited.add(curr)
                    last = curr
                    for nei in graph[curr]:
                        if nei not in visited:
                            q.append(nei)
            
            return diameter

        d1 = findDiameter(e1)
        d2 = findDiameter(e2)

        curr = max(d1, d2)

        return max(curr, ceil(d1/2) + ceil(d2/2) + 1)