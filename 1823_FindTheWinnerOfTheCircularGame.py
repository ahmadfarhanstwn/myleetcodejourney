class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        player = deque(range(1, n+1))
        index = 0
        while len(player) != 1:
            indexDel = (index + (k-1)) % len(player)
            del player[indexDel]
            index = indexDel
        return player[0]