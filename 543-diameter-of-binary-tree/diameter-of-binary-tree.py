# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = 0

        # def getDepth(root):
        #     nonlocal res
            
        #     if not root:
        #         return 0

        #     dl, dr = getDepth(root.left), getDepth(root.right)
        #     res = max(res, dl+dr)
        #     return max(dl,dr)+1

        # getDepth(root)
        # return res

        res = [0]
        self.getDepth(root, res)
        return res[0]

    def getDepth(self, node, res):
        if not node:
            return 0
        
        ldepth, rdepth = self.getDepth(node.left, res), self.getDepth(node.right, res)
        res[0] = max(res[0], ldepth+rdepth)
        return max(ldepth, rdepth) + 1

