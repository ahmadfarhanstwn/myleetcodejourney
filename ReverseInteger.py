class Solution:
    def reverse(self, x: int) -> int:
        output = []
        for i in str(x):
            if i != '-':
                output.insert(0, i)
        
        if int(''.join(output)) >= 2**31-1 or int(''.join(output)) <= -2**31:
            return 0
        if x < 0:
            return -int(''.join(output))
        else:
            return int(''.join(output))

##28 ms runtime