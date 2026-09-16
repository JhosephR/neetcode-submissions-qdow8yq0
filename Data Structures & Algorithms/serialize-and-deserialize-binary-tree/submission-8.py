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
        def preorder(node):
            if not node:
                data.append("n")
                return

            data.append(str(node.val))

            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(data)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "n":
            return None
        data = data.split(",")
        i = 0
        def preorder():
            nonlocal i
            if data[i] == "n":
                i += 1
                return
            
            root = TreeNode(data[i])
            i += 1

            root.left = preorder()
            root.right = preorder()
            return root
        return preorder()