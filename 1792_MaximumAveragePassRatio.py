class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        selisihList = []
        answer = 0
        for i in range(len(classes)):
            selisih = (((classes[i][0] + extraStudents) / (classes[i][1] + extraStudents))) - (classes[i][0] / classes[i][1])
            selisihList.append(selisih)
        
        maxSelisih = max(selisihList)
        maxSelisih = selisihList.index(maxSelisih)
        classes[maxSelisih][0] += extraStudents
        classes[maxSelisih][1] += extraStudents
        
        for x in range(len(classes)):
            answer += classes[x][0] / classes[x][1]
            
        return answer / len(classes)