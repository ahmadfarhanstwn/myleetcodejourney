class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1: return votes[0]
        point = {k:[0]*len(votes[0]) for k in votes[0]}
        output = ''
        for val in votes:
            for i,ch in enumerate(val):
                point[ch][i]-=1
        
        a = sorted(point.items(), key=lambda x: (x[1],x[0]))
        for ch,_ in a:
            output+=ch
        return output