class Solution:
    def exist(self, board, word):
        
            
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)
        visit = set()

        def dfs(i,j,c):
            
            if c==word_len:
                return True

            if min(i,j)<0 or i>rows-1 or j>cols-1 or c>word_len or board[i][j]!=word[c] or (i,j) in visit:
                return False

            # logic
            visit.add((i,j))
            
            #parsing
            if dfs(i,j+1,c+1) or dfs(i-1,j,c+1) or dfs(i+1,j,c+1) or dfs(i,j-1,c+1):
                return True

            visit.remove((i,j))
            return False

        for i in range(rows):
            for j in range(cols):
                if word[0] == board[i][j]:
                    if dfs(i,j,0):
                        return True    
        return False