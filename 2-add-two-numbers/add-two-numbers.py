# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 != None and l2 != None:
            added = l1.val + l2.val + carry
            ones = added%10
            carry = added//10

            curr.next = ListNode(ones)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            added = l1.val + carry
            ones = added%10
            carry = added//10

            curr.next = ListNode(ones)
            curr = curr.next
            l1 = l1.next

        while l2 != None:
            added = l2.val + carry
            ones = added%10
            carry = added//10

            curr.next = ListNode(ones)
            curr = curr.next
            l2 = l2.next
        
        if carry != 0:
            curr.next = ListNode(carry)
            
        return dummy.next
        


        