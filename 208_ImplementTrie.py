class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.theEndOfWords = False

class Trie:

    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
    
    def getIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        pCrawl = self.root
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.theEndOfWords = True

    def search(self, word: str) -> bool:
        pCrawl = self.root
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.theEndOfWords
            
    def startsWith(self, prefix: str) -> bool:
        pCrawl = self.root
        for i in range(len(prefix)):
            index = self.getIndex(prefix[i])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)