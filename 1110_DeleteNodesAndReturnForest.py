# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        output = []
        
        def rec(root, is_root):
            if not root:
                return None
            root_deleted = root.val in to_delete
            if is_root and not root_deleted:
                output.append(root)
            root.left = rec(root.left, root_deleted)
            root.right = rec(root.right, root_deleted)
            return None if root_deleted else root
        rec(root, True)
        return output