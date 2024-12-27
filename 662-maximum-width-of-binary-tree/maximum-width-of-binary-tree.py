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
            l, r = float("inf"), -1
            for _ in range(n):
                node, idx = q.popleft()
                if node.left: q.append((node.left, idx*2+1))
                if node.right: q.append((node.right, idx*2+2))
                l = min(l, idx)
                r = max(r, idx)
            
            if l!=float("inf") and r!=-1:
                res = max(res, r-l+1)

        return res
        