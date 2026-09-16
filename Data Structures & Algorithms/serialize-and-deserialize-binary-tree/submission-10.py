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
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                data.append("n")
        return ",".join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "n":
            return None
        data = data.split(",")
        root = TreeNode(data[0])
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if data[i] != "n":
                node.left = TreeNode(data[i])
                q.append(node.left)
            i += 1
            if data[i] != "n":
                node.right = TreeNode(data[i])
                q.append(node.right)
            i += 1
        return root