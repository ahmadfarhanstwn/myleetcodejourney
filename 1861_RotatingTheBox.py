class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            for j in range(len(box[i])-1,-1,-1):
                if box[i][j] == '.':
                    for z in range(j-1,-1,-1):
                        if box[i][z] == '#':
                            box[i][j] = '#'
                            box[i][z] = '.'
                            break
                        elif box[i][z] == '*':
                            break
        rotatedBox = []
        for m in range(len(box[0])):
            boxTemp = []
            for n in range(len(box)-1,-1,-1):
                boxTemp.append(box[n][m])
            rotatedBox.append(boxTemp)
        return rotatedBox