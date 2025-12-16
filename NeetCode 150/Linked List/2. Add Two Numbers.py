# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #numbers are in reverse order. We anyways add numbers in reverse order. Number returned is also in reverse order
        #or consider this as add both nodes and move carry forward/right side

        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            curr.next = ListNode(total%10)
            curr = curr.next

            carry = total // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

