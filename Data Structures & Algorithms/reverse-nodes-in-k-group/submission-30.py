# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = l1 = ListNode(0,head)

        while True:
            kth = self.kthNode(l1, k)
            if not kth:
                break
            
            l2 = kth.next
            prev = l2
            curr = l1.next
            while curr != l2:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            temp = l1.next
            l1.next = kth
            l1 = temp
        return dummy.next

    def kthNode(self, curr, n):
        while curr and n:
            curr = curr.next
            n -= 1
        return curr