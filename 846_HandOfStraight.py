from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand.sort()
        count = dict(Counter(hand))    
        for i in hand:
            if count[i] > 0:
                count[i] -= 1
                for z in range(i+1,i+groupSize):
                    if z not in count or count[z] < 1:
                        return False
                    else:
                        count[z] -= 1
        return True