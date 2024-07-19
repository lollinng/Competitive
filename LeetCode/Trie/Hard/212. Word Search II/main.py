class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root 
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word_end = True
                
class Solution:

    def dfs(self,row,col,trie_node,path,visited):
        rows = len(self.board)
        cols = len(self.board[0])


        if trie_node.word_end:
            self.res.add(path)

        visited.add((row,col))

        # loop
        for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            x,y = row+dx,col+dy
            if 0<=x<rows and 0<=y<cols and (x,y) not in visited and self.board[x][y] in trie_node.children:
                ch = self.board[x][y]
                self.dfs(x,y,trie_node.children[ch],path+ch,visited)
        
        visited.remove((row,col))


    def findWords(self, board, words):
        
        trie = Trie()
        self.res = set()
        self.board = board
        rows = len(board)
        cols = len(board[0])

        # run the trie insert
        for w in words:
            trie.insert(w)

        # loop over the 
        for row in range(rows):
            for col in range(cols):
                ch = board[row][col]
                if ch in trie.root.children:
                    visited = set()
                    self.dfs(row,col,trie.root.children[ch],ch,visited)

        return self.res