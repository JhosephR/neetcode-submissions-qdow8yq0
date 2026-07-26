# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:                     # Prevents running the loop if tree is "None"
            return []        
        ans = []
        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:             # Avoids pushing "None" children
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ans.append(level)
        return ans