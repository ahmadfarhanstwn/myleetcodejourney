class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure = set()
        for x in paths:
            departure.add(x[0])
            
        for x in paths:
            if x[1] in departure:
                continue
            else:
                return x[1]