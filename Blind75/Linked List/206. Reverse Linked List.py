# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive method
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next) # always the last node from the list is returned, so the new head is last node and we return that
        head.next.next = head
        head.next = None

        return new_head

        #Iterative method
        prev = None # Initially, there's no previous node
        curr = head  # Start from the head

        while curr:
            next_node = curr.next # Save next node
            curr.next = prev # Reverse the link
            prev = curr # Move prev forward
            curr = next_node # Move curr forward 

        return prev  # prev will be the new head

