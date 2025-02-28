"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.helper(root, None)
        return root

    def helper(self, node, nextNode):
        if not node:
            return
        node.next = nextNode
        self.helper(node.left, node.right)
        self.helper(node.right, None if not nextNode else nextNode.left)