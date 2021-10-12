class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # column
        for i in board:
            appear = []
            for j in i:
                if j in appear:
                    return False
                if j != '.':
                    appear.append(j)
        # row
        for i in range(len(board)):
            appear = []
            for j in range(len(board)):
                if board[j][i] in appear:
                    return False
                if board[j][i] != '.':
                    appear.append(board[j][i])
        # box
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                unit = [i for i in square if i != '.']
                if len(set(unit)) != len(unit):
                    return False
        return True