# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        unique = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.val not in unique:
                unique.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(root)
        unique.sort()
        if len(unique) > 1:
            return unique[1]
        return -1