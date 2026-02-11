# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        k %= length
        if k ==0:
            return head
        
        #make circular
        curr.next = head
        
        new_head = head
        for i in range(length - k - 1):
            new_head = new_head.next
        
        new_tail = new_head.next
        new_head.next = None

        return new_tail

