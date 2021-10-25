from collections import deque
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                root = i
        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])
        return len(visited) == n
    
        # MY ACCEPTED IF ROOT == 0
        # seto = set()
        # seto.add(0)
        # for i in range(len(leftChild)):
        #     if i not in seto:
        #         return False
        #     if leftChild[i] != -1 and leftChild[i] in seto:
        #         return False
        #     if rightChild[i] != -1 and rightChild[i] in seto:
        #         return False
        #     if leftChild[i] != -1 and leftChild[i] <= i:
        #         return False
        #     if rightChild[i] != -1 and rightChild[i] <= i:
        #         return False
        #     if leftChild[i] != -1:
        #         seto.add(leftChild[i])
        #     if rightChild[i] != -1:
        #         seto.add(rightChild[i])
        # return True