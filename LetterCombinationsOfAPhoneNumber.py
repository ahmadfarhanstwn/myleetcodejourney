class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        output = []
        temporarily = ''
        
        if len(digits) == 1:
            for a in dict[digits[0]]:
                output.append(a)
        elif len(digits) == 2:
            for a in dict[digits[0]]:
                for b in dict[digits[1]]:
                    temporarily = a + b
                    output.append(temporarily)
        elif len(digits) == 3:
            for a in dict[digits[0]]:
                for b in dict[digits[1]]:
                    for c in dict[digits[2]]:
                        temporarily = a + b + c
                        output.append(temporarily)
        elif len(digits) == 4:
            for a in dict[digits[0]]:
                for b in dict[digits[1]]:
                    for c in dict[digits[2]]:
                        for d in dict[digits[3]]:
                            temporarily = a + b + c + d
                            output.append(temporarily)
        
        return output
                