# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        q1 = deque([root])
        q2 = deque()
        s = set()

        while q1:
            for i in range(len(q1)):
                node = q1.popleft()
                q2.append(node)

                print(node.val)
                if node.val == p.val or node.val == q.val and node not in s:
                    if len(s) == 2:
                        q1 = deque()
                        break
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
        if p.val > q.val:
            p.val, q.val = q.val, p.val

        for node in q2:
            if p.val <= node.val <= q.val:
                return node