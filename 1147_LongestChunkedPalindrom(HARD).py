class Solution:
    def longestDecomposition(self, text: str) -> int:
        output = 0
        index = 0
        while index < len(text)-1:
            if text[index] == text[-1]:
                if text[:index+1] == text[-1*(index+1):]:
                    text = text[index+1:-1*(index+1)]
                    output += 2
                    index = 0
                else:
                    index += 1
            else:
                index += 1
        if len(text) != 0:
            output += 1
        return output