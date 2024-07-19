class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word=True

    def longest_common_prefix(self):
        prefix = ''
        node = self.root
        while node:
            if len(node.children)==1 and node.is_end_of_word==False:
                char,next_node = list(node.children.items())[0]
                prefix += char
                node = next_node
            else:
                break
        return prefix


class Solution:

    def longestCommonPrefix(self, strs):
        trie_obj = Trie()
        for word in strs:
            trie_obj.insert(word)
        return trie_obj.longest_common_prefix()