class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        output = 0
        if ruleKey == 'type':
            key = 0
        elif ruleKey == 'color':
            key = 1
        else:
            key = 2
        for i in items:
            if i[key] == ruleValue:
                output += 1
        return output
    
    #time complexity = O(n),where n=len(items)
    #spacecomplexity = O(1)