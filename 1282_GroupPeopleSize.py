class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dictionary = {}
        output = []
        for i in range(len(groupSizes)):
            if groupSizes[i] in dictionary:
                dictionary[groupSizes[i]].append(i)
            else:
                dictionary[groupSizes[i]] = []
                dictionary[groupSizes[i]].append(i)
        for m in dictionary:
            temp = []
            for n in dictionary[m]:
                if len(temp) == m:
                    output.append(temp)
                    temp = []
                temp.append(n)
            output.append(temp)
        return output
    
        # Time Complexity = O(n+n)
        # Space Complexity = O(n+n)