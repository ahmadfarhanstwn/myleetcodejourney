class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ''
        listPalindrome = list(palindrome)
        for i in range(len(listPalindrome)//2):
            if listPalindrome[i] != 'a':
                listPalindrome[i] = 'a'
                return ''.join(listPalindrome)
        listPalindrome[-1] = 'b'
        return ''.join(listPalindrome)