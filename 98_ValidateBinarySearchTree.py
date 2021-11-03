# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current = root
        stack = []
        visited = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                if visited:
                    if visited[-1] >= current.val:
                        return False
                visited.append(current.val)
                current = current.right
            else:
                break
        return True