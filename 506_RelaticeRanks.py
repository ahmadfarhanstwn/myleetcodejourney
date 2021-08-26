class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse= True)
        ranking = []
        for i in score:
            position = sortedScore.index(i) + 1
            if position == 3:
                ranking.append('Bronze Medal')
            elif position == 2:
                ranking.append('Silver Medal')
            elif position == 1:
                ranking.append('Gold Medal')
            else:
                ranking.append(str(position))
        return ranking