from statistics import multimode

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        path = []
        path.append(rounds[0])
        
        for i in range(1, len(rounds)):
            if rounds[i] >= rounds[i-1]:
                x = range(rounds[i-1]+1, rounds[i]+1)
                for b in x:
                    path.append(b)
            else:
                x = range(1, rounds[i]+1)
                y = range(rounds[i-1]+1, n+1)
                for z in y:
                    path.append(z)
                for b in x:
                    path.append(b)
        
        return sorted(multimode(path), key=int)
        