class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def checkUpper(string):
            return [s for s in string if s.isupper()]
        
        def checkSimilarity(q, p):
            for i in p:
                if i in q:
                    q = q[q.index(i)+1:]
                else:
                    return False
            return True
        
        return [checkUpper(q) == checkUpper(pattern) and checkSimilarity(q,pattern) for q in queries]