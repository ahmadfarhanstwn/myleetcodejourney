class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current = 0
        for i in logs:
            if i == "../" and current != 0:
                current -= 1
            elif i == "../" and current == 0:
                continue
            elif i == "./":
                continue
            else:
                current += 1
        return current