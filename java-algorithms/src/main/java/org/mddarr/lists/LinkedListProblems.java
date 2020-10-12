package org.mddarr.lists;

public class LinkedListProblems {
    public static void main(String[] args){
//        ListNode head = new ListNode(1);
//        head.next = new ListNode(2);
//        head.next.next = new ListNode(3);
//        head.next.next.next = new ListNode(4);
//        Solution solution = new Solution();
//        ListNode reversedList = solution.reverseList(head);
//        solution.reverseList(reversedList);


//        Solution solution = new Solution();
//        ListNode cyclicHead = new ListNode(1);
//        cyclicHead.next = new ListNode(2);
//        cyclicHead.next.next = new ListNode(3);
//        cyclicHead.next.next.next = new ListNode(1);
//        boolean iscyclic = solution.hasCycle(cyclicHead);
//        System.out.println("The linked list is cyclic " + iscyclic);
        Solution solution = new Solution();
        ListNode lhead = new ListNode(1);
//        lhead.next = new ListNode(2);
//        lhead.next.next = new ListNode(3);
//        lhead.next.next.next = new ListNode(4);
//        lhead.next.next.next.next = new ListNode(5);
        ListNode newHead = solution.rotateRight(lhead,1);

        solution.printList(newHead);

    }

}
