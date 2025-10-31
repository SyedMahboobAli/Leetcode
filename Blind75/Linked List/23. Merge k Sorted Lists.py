# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode()
        curr = dummy
        heap = []

        for i,node in enumerate(lists):
            if node: #imp, fails if any head is empty
                heapq.heappush(heap,(node.val,i,node))
                #here heappush can't compare node vs node, so type error. but with val it can and if tie, then list index, so always the earlie list number goes in if a tie and node vs node comp never happens => no failure
        
        while heap:
            val, i, node  = heapq.heappop(heap)
            curr.next=node
            curr=curr.next
            if(node.next):
                heapq.heappush(heap,(node.next.val,i,node.next))
                #we always have a track of which list the node is pushed
            
        return dummy.next

'''
Notes:
1. Brute force solution:

Collect all node values into an array. Sort them. Build a new linked list from sorted values.
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next

2. Merge lists one by one using merge 2 sorted lists code:

res = lists[0]
for i in range(1, len(lists)):
  res = merge(res, lists[i])
return res
'''
