class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.complete = False
    
    def __repr__(self):
        return str(self.childrens)
    

class Solution:
    """
    Intuition

    Since list of words can be 4*103 which will be hard to parse through and check if it exists
    we will use Trie datastructure

    we will iterate throgh matrix use backtracking and perform dfs with trie

    1) Insert the list of words in trie
    2) iteratre over matrix adn run dfs
    3) return if current matrix elment not in trie
    4) keep running dfs on element until we find node.complete marking word competed
    5) append the word to res if complete
    6) and keep the recursion going untill it gets out of trie or bounds
    7) Make sure of backtracking by using visit set
    8) add characters to found_word at each dfs/trie iteration

    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root
        
        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()
            curr = curr.childrens[c]
        curr.complete = True



    def findWords(self, board, words):
        rows = len(board)
        cols = len(board[0])
        word_len = len(words)
        # inserting to trie
        for word in words:
            self.insert(word)

        visit = set() 
        res = []
        # backtracking algroithm
        def dfs(i,j,found_word,node):
            

            # break
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in visit or (board[i][j] not in node.childrens):
                return
            
            

            # frontrack
            visit.add((i,j))
            found_word += board[i][j]
            
            new_node = node.childrens[board[i][j]]
            # logic done
            if new_node.complete:
                if found_word not in res:
                    res.append(found_word)
                
                

            # recursion
            dfs(i+1,j,found_word,node.childrens[board[i][j]])
            dfs(i,j+1,found_word,node.childrens[board[i][j]])
            dfs(i,j-1,found_word,node.childrens[board[i][j]])
            dfs(i-1,j,found_word,node.childrens[board[i][j]])
            
            # backtrack
            visit.remove((i,j))
           
            


        curr = self.root
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,"",curr)
        return res

