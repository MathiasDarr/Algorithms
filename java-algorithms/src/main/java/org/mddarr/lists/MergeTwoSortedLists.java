package org.mddarr.lists;



public class MergeTwoSortedLists {

    public static void main(String[] args) {
        ListNode head1 = new ListNode(1);

        head1.next = new ListNode(2);
        head1.next.next = new ListNode(4);

        ListNode head2 = new ListNode(1);
        head2.next = new ListNode(3);
        head2.next.next = new ListNode(4);


        Solution solution = new Solution();
        ListNode mergedListHead = solution.mergeTwoLists(head1, head2);
        solution.printList(mergedListHead);

    }





}
