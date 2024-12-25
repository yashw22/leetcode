# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def getSwaps(ls):
            n = len(ls)
            count = 0

            target = sorted(ls)
            pos = {val:idx for idx, val in enumerate(ls)}

            for i in range(n):
                if ls[i] != target[i]:
                    count += 1
                    
                    curr = pos[target[i]]
                    pos[ls[i]] = curr
                    ls[curr] = ls[i]

            return count


        q = deque([root])
        count = 0

        while q:
            n = len(q)
            row = []

            for _ in range(n):
                curr = q.popleft()
                row.append(curr.val)
                
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            
            count += getSwaps(row)

        return count