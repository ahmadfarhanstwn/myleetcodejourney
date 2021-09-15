"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        if root != None:
            res = []
            for child in root.children:
                res += self.postorder(child)
            output += res
            output.append(root.val)
        return output