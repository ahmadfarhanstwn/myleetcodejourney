class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict = {}
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        a = dict.values()
        sortedA = sorted(list(a), reverse=True)
        output, index, constraint = 0, 0, len(arr)//2
        while output < constraint:
            output += sortedA[index]
            index += 1
        return index