class TrieNode:
    def __init__(self):
        self.children = {}
        self.complete = False

    def __repr__(self):
        return str(self.children)

'''
Intuition:
We are here trying to build a prefix tree which stores character of its insertion 
'''
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # iterating and insertign every character of word in trie
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() # each children of node will be another node 
            curr = curr.children[c]
        curr.complete = True
        # print(self.root)


    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            
        return curr.complete

    def startsWith(self, prefix):
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)