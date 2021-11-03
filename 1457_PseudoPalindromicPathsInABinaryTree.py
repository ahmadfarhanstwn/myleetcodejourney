# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        output = 0
        queue = deque()
        dick = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        dick[root.val] += 1
        queue.append((root,dick))
        while queue:
            node,dicky = queue.popleft()
            if not node.left and not node.right:
                odd = 0
                for i in range(1,10):
                    if dicky[i] % 2 == 1:
                        odd += 1
                if odd <= 1:
                    output += 1
            if node.left:
                dickLeft = dict(dicky)
                dickLeft[node.left.val] += 1
                queue.append((node.left,dickLeft))
            if node.right:
                dickRight = dict(dicky)
                dickRight[node.right.val] += 1
                queue.append((node.right,dickRight))
        return output