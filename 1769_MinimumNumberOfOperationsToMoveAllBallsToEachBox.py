class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = [0] * len(boxes)
        leftCount, leftSum, rightCount, rightSum = 0,0,0,0
        for i in range(1,len(boxes)):
            if boxes[i-1] == '1':
                leftCount += 1
            leftSum += leftCount
            output[i] = leftSum
        for i in range(len(boxes)-2,-1,-1):
            if boxes[i+1] == '1':
                rightCount += 1
            rightSum += rightCount
            output[i] += rightSum
        return output