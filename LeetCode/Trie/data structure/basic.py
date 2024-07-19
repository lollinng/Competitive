class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0  # to keep track of number of words under this node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count +=1                     # Increment count for each node visited
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def count_words_with_prefix(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.count
    
    def _dfs(self,node,prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)

        # getting key_Valye pairs from the current nodes children dict
        for char,next_node in node.children.items():
            # adding character to prefix to letter send as autocomplete word
            words.extend(self.dfs(next_node,prefix+char))
        
        return words

    def auto_complete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        # sending prefix to remember current character upon which other character will be updated
        return self._dfs(node,prefix)
    
    def longest_common_prefix(self):
        prefix = ""
        node = self.root
        while node:
            # if prefix same as in only one path in trie and not one word ended
            if len(node.children)==1 and node.is_end_of_word==False:
                # then itertae down more , dince only one child
                char,next_node = list(node.children.items())[0]
                prefix+=char
                node = next_node
            else:
                break
        return prefix
    
    def delete_node(self,word):
        
        # should we delete its child node
        def _delete_helper(node,word,index):
            
            # IF we reach the word
            if len(word) == index:
                # if word doesnt exist
                if node.is_end_of_word == False:
                    return False

                # if word exist
                node.is_end_of_word = False
                # and the word doesn't have any children
                return len(node.children)==0  
    

            
            character = word[index]  # get next word character
            # if character doesn't exist in trie
            if character not in node.children:
                return False

            should_delete = _delete_helper(node.children[character],word,index+1)

            # if should delete
            if should_delete:
                del node.children[character]
                # if no more childrens of current node then delete it
                # since the word below is already deleted in above line  
                return len(node.children)==0

            # if shouldn't delete
            return False

        return  _delete_helper(self.root,word,0)

    
    

# Create a new Trie
trie = Trie()

# Set of strings to insert
words = ["apple", "app", "application", "bat", "ball", "batman"]

# Insert each word into the Trie
for word in words:
    trie.insert(word)

# Search for words
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("appl"))   # Output: False

# Check if any word starts with a given prefix
print(trie.starts_with("app"))  # Output: True
print(trie.starts_with("apl"))  # Output: False


