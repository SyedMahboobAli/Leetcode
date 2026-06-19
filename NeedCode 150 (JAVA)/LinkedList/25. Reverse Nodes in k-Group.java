/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k<=1) return head;

        ListNode dummy = new ListNode(0,head);

        ListNode groupPrev = dummy;

        while(true){
            ListNode kth = getkth(groupPrev,k);
            if (kth == null) break;

            ListNode groupNext  = kth.next;

            //reverse the group
            ListNode curr = groupPrev.next;
            ListNode prev = groupNext;

            while(curr != groupNext){
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }

            //reconnect

            ListNode temp = groupPrev.next;
            groupPrev.next = kth;
            groupPrev = temp;
        }
        return dummy.next;
    }

    private ListNode getkth(ListNode start, int k){
        while(start != null && k >0){
            start = start.next;
            k--;
        }
        return start;
    }
}
