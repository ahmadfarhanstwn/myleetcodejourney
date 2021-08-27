class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        output = 0
        for i in grid:
            for x in i:
                if x < 0:
                    output += 1
        return output