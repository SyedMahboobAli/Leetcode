# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        
        # Step 1: Find middle using slow and fast pointers
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # Step 2: Reverse the second half
        prev=None
        curr=slow.next #div is always like [1,2,3] [1,2]
        slow.next=None #imp # Split the list into two halves
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        
         # Step 3: Merge two halves
        first=head
        second=prev
        while second: #since the div is always like [1,2,3] [1,2]
            tmp1,tmp2=first.next,second.next
            first.next = second
            second.next=tmp1
            first,second=tmp1,tmp2
        
