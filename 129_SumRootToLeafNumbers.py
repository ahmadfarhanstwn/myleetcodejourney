# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return root.val
        if root.left:
            root.left.val += 10*root.val
        if root.right:
            root.right.val += 10*root.val
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)