# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        carry = 0

        while l1 and l2:
            sm = l1.val + l2.val + carry
            carry = sm // 10
            sm = sm % 10
            tail.next = ListNode(sm)

            l1, l2 = l1.next, l2.next
            tail = tail.next

        l1 = l1 or l2
        while l1:
            sm = l1.val + carry
            carry = sm // 10
            sm = sm % 10
            tail.next = ListNode(sm)

            l1 = l1.next
            tail = tail.next
        
        if carry:
            tail.next = ListNode(carry)

        return dummy.next