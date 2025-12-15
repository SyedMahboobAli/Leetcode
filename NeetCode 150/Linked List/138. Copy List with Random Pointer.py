"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Approach 2 without hashmap (Node Weaving: adding intermediary nodes)
        if not head:
            return head
         # 1) Create new nodes and insert after each original
        curr=head
        while curr:
            new_node = Node(curr.val) # clone current node
            new_node.next = curr.next # link clone to next
            curr.next = new_node # place clone after original
            curr = new_node.next # move to next original
        
        #2) Assign random pointers for the cloned nodes
        curr = head
        while curr:
            if curr.random:
                # clone.random = original.random.next (its clone)
                curr.next.random = curr.random.next
            curr = curr.next.next # skip to next original node
        
        # 3) Separate the cloned list from the original
        curr = head
        copy_head = head.next
        copy_curr = copy_head

        while curr:
            curr.next = curr.next.next  # restore original list
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next # link clone nodes together
            curr = curr.next
            copy_curr = copy_curr.next
        
        return copy_head

        #Approach 1: Hashmap
        map = {None:None} #edge case : when none is reached while checking curr.next, we need map[None] as well

        curr = head
        while curr:
            copy = Node(curr.val)
            map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            #all pointings are to the copy nodes
            copy = map[curr]
            copy.next = map[curr.next]
            copy.random = map[curr.random]
            curr = curr.next
        
        return map[head]
