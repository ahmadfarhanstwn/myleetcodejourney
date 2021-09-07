class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        index = 0
        for i in range(1,min(n+1,target[-1]+1)):
            if i == target[index]:
                output.append('Push')
                index += 1
            else:
                output.append('Push')
                output.append('Pop')
        return output
        
        # time complexity = O(n)
        # space complexity = O(m), m = len(output)