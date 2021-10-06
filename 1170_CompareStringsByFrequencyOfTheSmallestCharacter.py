class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        a = [i.count(min(i)) for i in queries]
        b = sorted([j.count(min(j)) for j in words])
        output = []
        for x in a:
            l, r = 0, len(b)-1
            while l <= r:
                mid = (l + r) // 2
                if b[mid] <= x:
                    l = mid + 1
                else:
                    r = mid - 1
            output.append(len(b)-l)
        return output