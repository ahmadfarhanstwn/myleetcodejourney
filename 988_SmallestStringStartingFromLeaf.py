# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if root:
            if not root.left and not root.right:
                return chr(root.val+97)
            if root.left and not root.right:
                return self.smallestFromLeaf(root.left) + chr(root.val+97)
            if root.right and not root.left:
                return self.smallestFromLeaf(root.right) + chr(root.val+97)
            return min(self.smallestFromLeaf(root.left) + chr(root.val+97),self.smallestFromLeaf(root.right) + chr(root.val+97))