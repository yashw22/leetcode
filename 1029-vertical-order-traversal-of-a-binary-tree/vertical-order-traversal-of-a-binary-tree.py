# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        store = {}

        q = deque([(root, 0, 0)])

        while q:
            n = len(q)

            for _ in range(n):
                node, level, idx = q.popleft()
                if idx not in store:
                    store[idx] = [(level, node.val)]
                else:
                    store[idx].append((level, node.val))
                
                if node.left: q.append((node.left, level+1, idx-1))
                if node.right: q.append((node.right, level+1, idx+1))


        res = []
        for key in sorted(store.keys()):
            res.append([t[1] for t in sorted(store[key])])
        return res

