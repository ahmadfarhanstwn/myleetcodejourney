"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        output = root
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                else:
                    root.right.next = None
                root = root.next
            root = next
        return output