# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        
        if not lists:
            return None
 
        nodes = []
        for index,node in enumerate(lists):
            if node:
                heapq.heappush(nodes,(node.val,index))
        
        result = curr = ListNode(0)
        while nodes:
            value,node_index = heapq.heappop(nodes)
            node = lists[node_index]
            curr.next = node
            curr = curr.next
            
            if node.next:
                next_node = node.next
                heapq.heappush(nodes,(next_node.val,node_index))
                lists[node_index] = lists[node_index].next 

        return result.next


