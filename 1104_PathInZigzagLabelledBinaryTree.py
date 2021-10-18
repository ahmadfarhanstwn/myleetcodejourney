class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        n = 0
        output = []
        while label >= 2**n:
            n += 1
        n -= 1
        while n >= 0:
            output.append(int(label))
            if label % 2 == 1:
                label -= 1
            label = ((2**n)-1) - ((label-(2**n))/2)
            n -= 1
        return output[::-1]