class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dict = {
            'a' : 1,
            'b' : 2,
            'c' : 3,
            'd' : 4,
            'e' : 5,
            'f' : 6,
            'g' : 7,
            'h' : 8,
        }
        
        coordinate1 = dict[coordinates[0]]
        coordinate2 = int(coordinates[1])
        
        if (coordinate1 % 2 == 0 and coordinate2 % 2 == 1) or (coordinate1 % 2 == 1 and coordinate2 % 2 == 0):
            return True
        return False