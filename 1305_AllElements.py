# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        visited = []
        q1 = deque()
        q2 = deque()
        if root1:
            q1.append(root1)
        if root2:
            q2.append(root2)
        while q1:
            node = q1.popleft()
            visited.append(node.val)
            if node.left:
                q1.append(node.left)
            if node.right:
                q1.append(node.right)
        while q2:
            node = q2.popleft()
            visited.append(node.val)
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        return sorted(visited)
            