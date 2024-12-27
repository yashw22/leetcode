# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        res = 0

        while q:
            n = len(q)
            l, r = 0, 0
            for i in range(n):
                node, idx = q.popleft()
                if node.left: q.append((node.left, idx*2+1))
                if node.right: q.append((node.right, idx*2+2))
                if i==0: l=idx
                if i==n-1: r=idx
            
            res = max(res, r-l+1)

        return res
        