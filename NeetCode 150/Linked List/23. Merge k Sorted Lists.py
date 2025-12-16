# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        dummy = ListNode()
        curr = dummy

        #to add only head of each list
        for i,node in enumerate(lists):
            if node: # To handle null head
                heapq.heappush(heap,(node.val,i,node))
                #node.val to compare, then i to select list if tie between node.val and last node. we can't compare node vs node
            
        while heap:
            val,i,node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        
        return dummy.next
