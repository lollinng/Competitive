class TrieNode:
    def __init__(self):
        self.children = {}
        self.complete = False

    def __repr__(self):
        return str(self.children)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
               curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.complete = True

    def search(self, word: str) -> bool:
        curr = self.root
        word_len = len(word)
        def dfs(node,c):

                # if index of word equals len of word,all search good
                # check if its full word and return
                if c==word_len:
                    return node.complete

                # if replacement then dfs every node in the children of current node
                if word[c]=='.':
                    for new_node in node.children.values():
                        if dfs(new_node,c+1):
                            return True
                
                # if char in current children node run algorithm for next node
                if word[c] in node.children:
                    new_node = node.children[word[c]]
                    if dfs(new_node,c+1) :
                        return True 
                # else return false
                return False
       
        return dfs(curr,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)