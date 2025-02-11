# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []

        # res = []
        # q = deque()
        # q.append(root)

        # while q:
        #     n = len(q)
        #     curr = []
        #     for _ in range(n):
        #         node = q.popleft()
        #         curr.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(curr)

        # return res

        # res = []

        res = []

        def dfs(node, d):
            if not node:
                return
            
            if len(res)==d:
                res.append([])

            res[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)

        dfs(root, 0)
        return res