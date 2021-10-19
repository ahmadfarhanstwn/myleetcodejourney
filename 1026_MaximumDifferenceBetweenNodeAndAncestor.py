# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper(root)
        
    def helper(self, root, mn = 10001, mx = 0):
        if not root:
            return mx - mn
        mx = max(mx, root.val)
        mn = min(mn, root.val)
        return max(self.helper(root.left, mn, mx), self.helper(root.right, mn, mx))