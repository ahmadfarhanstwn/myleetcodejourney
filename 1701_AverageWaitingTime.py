class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        summy = 0
        start = customers[0][0]
        for i in customers:
            start = max(start,i[0])
            start += i[1]
            summy += start - i[0]
        return summy / (len(customers))