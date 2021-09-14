# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        value = []
        def inOrder(node):
            if node.left: inOrder(node.left)
            value.append(node.val)
            if node.right: inOrder(node.right)
        inOrder(root)
        output = max(value)
        for i in range(1,len(value)):
            output = min(output, value[i]-value[i-1])
        return output