class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {'a', 'e', 'i', 'o', 'u'}
        output, index = 0, 0
        for i in range(k):
            if s[i] in vow:
                output += 1
        vowel = output
        for i in range(k, len(s)):
            if s[index] in vow:
                vowel -= 1
            if s[i] in vow:
                vowel += 1
            index += 1
            output = max(output, vowel)
        return output