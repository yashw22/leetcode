"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if not node:
        #     return None

        # visited = {}

        # def dfs(old):
        #     if old.val in visited:
        #         return visited[old.val]
            
        #     curr = Node(old.val)
        #     visited[curr.val] = curr
        #     for node in old.neighbors:
        #         curr.neighbors.append(dfs(node))
            
        #     return curr

        # return dfs(node)

        if not node:
            return None

        visited = {}
        def dfs(old):
            if old.val in visited:
                return visited[old.val]

            curr = Node(old.val)
            visited[curr.val] = curr

            for nei in old.neighbors:
                curr.neighbors.append(dfs(nei))

            return curr
            
        return dfs(node)