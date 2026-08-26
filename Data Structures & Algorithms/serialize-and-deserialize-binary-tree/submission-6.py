# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "n"
        data = []
        def dfs(node):
            if not node:
                data.append("n")
                return
            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "n":
            return None
        vals = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if vals[i] == "n":
                i += 1
                return
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()