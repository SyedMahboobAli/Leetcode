# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #solution 2: recursion
        if not list1:
            return list2
        if not list2:
            return list1
        
        if (list1.val < list2.val):
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2


        #this creates a node with val =0 and next=None
        dummy = ListNode () 
        curr = dummy #curr moves forward while dummy points to head which will be used while returning

        while list1 and list2:
            if (list1.val < list2.val):
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # now either list1 or list2 is empty. so which ever is left add
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next #since first is 0,none
