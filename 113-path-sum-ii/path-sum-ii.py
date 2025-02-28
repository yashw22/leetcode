# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(node, currSum):
            if not node:
                return

            val = node.val
            curr.append(val)

            # if currSum+val == targetSum:
            #     print(curr)
            #     res.append(curr[:])

            if not node.left and not node.right and currSum+val == targetSum:
                print(curr)
                res.append(curr[:])

            dfs(node.left, currSum+val)
            dfs(node.right, currSum+val)
            

            curr.pop()

        dfs(root, 0)
        return res

        