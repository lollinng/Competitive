from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        if node is None:
            return node

        def dfs(root):
            
            if root.val in nodes:
                return nodes[root.val]

            node_clone = Node(root.val,[])
            nodes[root.val] = node_clone

            for child_node in root.neighbors:
                node_clone.neighbors.append(dfs(child_node))
                        
            return node_clone
            

        return  dfs(node)
            