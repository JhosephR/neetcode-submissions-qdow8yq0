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
        nodeMap = defaultdict(lambda: Node(0))
        nodeMap[None] = None
        curr = head

        while curr:
            nodeMap[curr].val = curr.val
            nodeMap[curr].next = nodeMap[curr.next]
            nodeMap[curr].random = nodeMap[curr.random]
            curr = curr.next
        return nodeMap[head]