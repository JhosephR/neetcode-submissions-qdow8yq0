# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = g1 = ListNode(0, head)

        while True:
            kth = self.findKnode(g1, k)
            if not kth:
                break
            
            g2 = kth.next
            prev, curr = g2, g1.next
            while curr != g2:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = g1.next
            g1.next = kth
            g1 = tmp
        return dummy.next

    def findKnode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr