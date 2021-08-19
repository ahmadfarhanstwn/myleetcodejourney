class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        output = 0
        
        for i, x in enumerate(board):
            if 'R' in x:
                rookX, rookY = i, x.index('R')
                    
        for i in range(rookY+1, len(board[rookX])):
            if board[rookX][i] == 'p':
                output += 1
                break
            elif board[rookX][i] == 'B':
                break
        
        for i in range(rookY-1, -1, -1):
            if board[rookX][i] == 'p':
                output += 1
                break
            elif board[rookX][i] == 'B':
                break
                
        for i in range(rookX-1, -1, -1):
            if board[i][rookY] == 'p':
                output += 1
                break
            elif board[i][rookY] == 'B':
                break
                
        for i in range(rookX+1, len(board)):
            if board[i][rookY] == 'p':
                output += 1
                break
            elif board[i][rookY] == 'B':
                break
                
        return output