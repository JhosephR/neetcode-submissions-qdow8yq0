"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy = defaultdict(lambda: Node(0))
        copy[None] = None

        curr = head
        while curr:
            copy[curr].val = curr.val           #[curr].next = new copy
            copy[curr].next = copy[curr.next]   #[curr.next] = original
            copy[curr].random = copy[curr.random]
            curr = curr.next
        
        return copy[head]