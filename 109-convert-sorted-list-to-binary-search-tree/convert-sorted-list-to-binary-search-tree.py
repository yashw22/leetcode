# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        return self.helper(head, None)

    def helper(self, head, tail):
        if head==tail:
            return None
        mid = self.getMid(head, tail)
        root = TreeNode(mid.val)
        root.left = self.helper(head, mid)
        root.right = self.helper(mid.next, tail)

        return root
        
    def getMid(self, head, tail):
        if not head:
            return None
        slow, fast = head, head

        while fast!=tail and fast.next!=tail:
            slow = slow.next
            fast = fast.next.next

        return slow
