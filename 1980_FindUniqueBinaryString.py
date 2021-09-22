class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if nums == ["0"]: return '1'
        bit = len(nums[0])
        lengthOfBit = '{:0' + str(bit) + 'b}'
        for i in range((2**bit)-1):
            if lengthOfBit.format(int(i)) not in nums:
                return lengthOfBit.format(int(i))
            
        ## Time Complexity = O(2**n)