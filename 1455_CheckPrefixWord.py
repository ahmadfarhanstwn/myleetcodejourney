class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentenceList = list(sentence.split(' '))
        
        for i in range(len(sentenceList)):
            if sentenceList[i][:len(searchWord)] == searchWord:
                return i + 1
            
        return -1