class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        b = dict(sorted(Counter(arr).items(), key=lambda item: item[1]))
        c = []
        for i in b:
            if k >= b[i]:
                k -= b[i]
                c.append(i)
            else:
                break
            if k < 1:
                break
        return len(b)-len(c)