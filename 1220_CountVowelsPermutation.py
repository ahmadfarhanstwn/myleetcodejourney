class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowel = {'a': 1, 'e': 1,'i':1,'o':1,'u':1}
        for i in range(1,n):
            a = vowel['a'] 
            e = vowel['e']
            i = vowel['i']
            o = vowel['o']
            u = vowel['u']
            vowel['a'] = e + i + u
            vowel['e'] = a + i
            vowel['i'] = e + o
            vowel['o'] = i
            vowel['u'] = i + o
        return (vowel['a'] + vowel['e'] + vowel['i'] + vowel['o'] + vowel['u']) % (10**9 + 7)