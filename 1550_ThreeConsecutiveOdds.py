class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddConsecutive = 0
        for i in arr:
            if oddConsecutive == 3:
                return True
            if i % 2 == 1:
                oddConsecutive += 1
            else:
                oddConsecutive = 0
        if oddConsecutive > 2:
            return True
        return False