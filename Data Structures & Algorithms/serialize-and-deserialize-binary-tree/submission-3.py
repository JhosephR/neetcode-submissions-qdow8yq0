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
        #level-order serialization
        q, data = deque([root]), []
        while q:
            node = q.popleft()
            if not node:
                data.append("n")
            else:    
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(data)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "n":
            return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "n":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "n":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root