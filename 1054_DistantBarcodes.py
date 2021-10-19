class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        barcodes.sort(key = lambda x: (count[x],x))
        barcodes[1::2], barcodes[::2] = barcodes[:len(barcodes)//2], barcodes[len(barcodes)//2:]
        return barcodes