from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count = dict(Counter(secret))
        bulls = cows = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                count[secret[i]] -= 1
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                continue
            elif guess[i] in count and count[guess[i]] > 0:
                cows += 1
                count[guess[i]] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
    
    #Time Complexity = O(n+n)
    #Space Complexity = O(unique), unique is the unique element in secret
    