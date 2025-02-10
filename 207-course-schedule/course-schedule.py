class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if not prerequisites:
            # return True

        # indeg = [0]*numCourses
        # adj = {i:[] for i in range(numCourses)}
        # for course, prereq in prerequisites:
        #     adj[prereq].append(course)
        #     indeg[course] += 1

        # q = deque()
        # done = 0
        # for i in range(numCourses):
        #     if indeg[i]==0:
        #         q.append(i)
        # while q:
        #     n= len(q)
        #     for _ in range(n):
        #         curr = q.popleft()
        #         done += 1
        #         for nei in adj[curr]:
        #             indeg[nei] -= 1
        #             if indeg[nei]==0:
        #                 q.append(nei)

        # return done == numCourses

        # if not prerequisites:
        #     return True

        # adj = {i: [] for i in range(numCourses)}
        # for course, prereq in prerequisites:
        #     adj[prereq].append(course)

        # visited = set()
        # def dfs(node):
        #     if node in visited:
        #         return False
        #     if not adj[node]:
        #         return True
            
        #     visited.add(node)
        #     for nei in adj[node]:
        #         if not dfs(nei):
        #             return False

        #     visited.remove(node)
        #     adj[node] = []
        #     return True
            
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True

        if not prerequisites:
            return True
        
        adj = {i:[] for i in range(numCourses)}
        indeg = [0]*numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indeg[u] += 1

        q = deque()
        for i in range(numCourses):
            if indeg[i]==0:
                    q.append(i)

        done = 0
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                done += 1
                for nei in adj[curr]:
                    indeg[nei] -= 1
                    if indeg[nei]==0:
                        q.append(nei)
        
        return done==numCourses
                



            
            

