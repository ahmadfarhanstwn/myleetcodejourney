class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        longest = ''
        substring = ''
        for i in range(len(s)):
            if s[i] not in substring:
                substring += s[i]
            else:
                if len(substring) > len(longest):
                    longest = substring
                substring = substring[substring.index(s[i])+1:] + s[i]
        if len(substring) > len(longest):
                    longest = substring
        return len(longest)