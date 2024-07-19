"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q, clones = deque([node]), {node.val:Node(node.val,[])}

        while q:
            curr = q.pop()
            curr_clone = clones[curr.val]

            for child_node in curr.neighbors:
                if child_node.val not in clones:
                    q.append(child_node)
                    clones[child_node.val] = Node(child_node.val,[])
               
                curr_clone.neighbors.append(clones[child_node.val])

        return clones[node.val]

            