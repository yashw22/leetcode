# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if not head:
        #     return None
        
        # curr = head
        # n = k

        # while n:
        #     if not curr:
        #         return self.rotateRight(head, k%(k-n))
        #     n -= 1
        #     curr = curr.next

        # temp = head
        # while curr.next:
        #     curr = curr.next
        #     temp = temp.next

        # curr.next = head
        # head = temp.next
        # temp.next = None

        # return head

        if not head or k==0:
            return head

        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1

        if k>=l:
            return self.rotateRight(head, k%l)

        temp = curr = head

        for _ in range(k):
            temp = temp.next

        while temp.next:
            temp = temp.next
            curr = curr.next

        temp.next = head
        head = curr.next
        curr.next = None

        return head