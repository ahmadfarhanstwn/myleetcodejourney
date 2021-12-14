class Solution:
    original = []
    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffled = self.original[:]
        for i in range(len(shuffled)):
            random = randrange(0,len(shuffled))
            prev = shuffled[i]
            shuffled[i] = shuffled[random]
            shuffled[random] = prev
        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()