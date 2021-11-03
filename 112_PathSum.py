# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque()
        q.append((root,root.val))
        while q:
            node,summy = q.popleft()
            if not node.left and not node.right and summy == targetSum:
                return True
            if node.left:
                q.append((node.left, node.left.val+summy))
            if node.right:
                q.append((node.right, node.right.val+summy))
        return False