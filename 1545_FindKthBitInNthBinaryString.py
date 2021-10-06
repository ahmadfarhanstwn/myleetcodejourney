class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        arr = []
        arr.append('0')
        for i in range(1,n):
            arr.append(arr[i-1] + '1' + ''.join('1' if x == '0' else '0' for x in arr[i-1][::-1]))
        return arr[n-1][k-1]