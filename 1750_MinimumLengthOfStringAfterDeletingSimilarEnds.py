class Solution:
    def minimumLength(self, s: str) -> int:
        left, right, output = 0, len(s)-1, len(s)
        while left < right:
            deletedElements = 0
            if s[left] != s[right]:
                return output
            deletedElements += 2
            lefty, righty = left+1, right-1
            while lefty < right:
                if s[lefty] != s[left]:
                    break
                else:
                    deletedElements += 1
                    lefty += 1
            while righty > lefty:
                if s[righty] != s[right]:
                    break
                else:
                    deletedElements += 1
                    righty -= 1
            output -= deletedElements
            left, right = lefty, righty
        return output