class Solution:
    def romanToInt(self, s: str) -> int:
        newS = list(s)
        output = 0
        dict = {
            'I': 1,
            'i': -1,
            'V': 5,
            'X': 10,
            'x': -10,
            'L': 50,
            'C': 100,
            'c': -100,
            'D': 500,
            'M': 1000,
        }
        
        for x in range(len(newS)-1):
            if newS[x] == 'I' and (newS[x+1] == 'V' or newS[x+1] == 'X'):
                newS[x] = 'i'
            elif newS[x] == 'X' and (newS[x+1] == 'L' or newS[x+1] == 'C'):
                newS[x] = 'x'
            elif newS[x] == 'C' and (newS[x+1] == 'D' or newS[x+1] == 'M'):
                newS[x] = 'c'
            
        for i in newS:
            output += dict[i]
            
        return output