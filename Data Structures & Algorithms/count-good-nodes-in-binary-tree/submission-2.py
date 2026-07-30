# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack, seen, ans = [root], {None:0}, 0
        maxStack = [root.val]
        while stack:
            node = stack[-1]
            if node.left not in seen:
                stack.append(node.left)
                maxStack.append(max(node.left.val, maxStack[-1]))
            elif node.right not in seen:
                stack.append(node.right)
                maxStack.append(max(node.right.val, maxStack[-1]))
            else:
                node = stack.pop()
                mxNode = maxStack.pop()
                if node.val >= mxNode:
                    ans += 1
                seen[node] = 1

        return ans
