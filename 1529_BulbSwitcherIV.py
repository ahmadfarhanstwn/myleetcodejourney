class Solution:
    def minFlips(self, target: str) -> int:
        initial = "0"
        output = 0
        for i in target:
            if i != initial:
                output += 1
                initial = "1" if initial == "0" else "0"
        return output
    
    ## Time Complexity = O(n)
    ## Space Complexity = O(1)