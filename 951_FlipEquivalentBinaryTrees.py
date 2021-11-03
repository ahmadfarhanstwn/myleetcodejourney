# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        qroot1 = deque()
        qroot2 = deque()
        c1 = dict.fromkeys([i for i in range(0,100)])
        c2 = dict.fromkeys([i for i in range(0,100)])
        if root1:
            qroot1.append(root1)
        if root2:
            qroot2.append(root2)
        while qroot1:
            node = qroot1.popleft()
            arr = []
            if node.left:
                arr.append(node.left.val)
                qroot1.append(node.left)
            if node.right:
                arr.append(node.right.val)
                qroot1.append(node.right)
            arr.sort()
            c1[node.val] = arr
        while qroot2:
            node = qroot2.popleft()
            arr = []
            if node.left:
                arr.append(node.left.val)
                qroot2.append(node.left)
            if node.right:
                arr.append(node.right.val)
                qroot2.append(node.right)
            arr.sort()
            c2[node.val] = arr
        return c1 == c2