# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # def dfs(node, mn, mx):
        #     if not node:
        #         return True

        #     if not (mn < node.val < mx):
        #         return False
            
        #     return dfs(node.left, mn, node.val) and dfs(node.right, node.val, mx)

        # return dfs(root, float("-inf"),  float("inf"))

        def dfs(curr, mn, mx):
            if not curr:
                return True
            if not (mn<curr.val<mx):
                return False
            return dfs(curr.left, mn, curr.val) and dfs(curr.right, curr.val, mx)

        return dfs(root, float("-inf"), float("inf"))