# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxim, level, maxLevel = -float('inf'), 0, 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            level += 1
            summy = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                summy += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if maxim < summy:
                maxim, maxLevel = summy, level
        return maxLevel