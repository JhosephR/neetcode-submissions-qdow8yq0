# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        nodeMap = {None: (0,0)}
        diameter = 0

        while stack:
            node = stack[-1]
            if node.left not in nodeMap:
                stack.append(node.left)
            elif node.right not in nodeMap:
                stack.append(node.right)
            else:
                node = stack.pop()
                l_h, l_d = nodeMap[node.left]
                r_h, r_d = nodeMap[node.right]
                diameter = max(diameter, l_h + r_h)
                nodeMap[node] = (1 + max(l_h, r_h), diameter)
        return nodeMap[root][1]