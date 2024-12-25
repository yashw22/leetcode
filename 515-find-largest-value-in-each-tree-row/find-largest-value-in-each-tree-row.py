# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None: return []
        res = []

        q = deque([root])

        while q:
            n = len(q)

            largest = q[0].val
            for _ in range(n):
                curr = q.popleft()
                largest = max(largest, curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

            res.append(largest)

        return res