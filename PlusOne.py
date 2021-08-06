class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = [str(digit) for digit in digits]
        integer = int("".join(string)) + 1
        backtolist = [int(digit) for digit in str(integer)]
        return backtolist