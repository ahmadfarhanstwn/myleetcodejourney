# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        def traverse(root):
            if not root: return 0
            subtreeSum = root.val + traverse(root.left) + traverse(root.right)
            output[subtreeSum] += 1
            return subtreeSum
        output = collections.Counter()
        traverse(root)
        maxOutput = max(output.values())
        return [s for s in output if output[s] == maxOutput]