# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node before head to simplify edge cases
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy

        # Move fast pointer n+1 steps ahead
        for i in range(n+1):
            fast=fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast=fast.next
            slow=slow.next
        #slow.next is the node to delete as we start from dummy
        slow.next = slow.next.next
        # Return the new head
        return dummy.next
