/*
  Merge two linked lists
  head pointer input could be NULL as well for empty list
  Node is defined as
  class Node {
     int data;
     Node next;
  }
*/

Node mergeLists(Node headA, Node headB) {
     // This is a "method-only" submission.
     // You only need to complete this method
    if (headA == null && headB == null) {
        return null;
    }
    else if (headA != null && headB == null) {
        return headA;
    }
    else if (headA == null && headB != null) {
        return headB;
    }
    else {
        Node newHead = new Node();
        if (headA.data <= headB.data) {
            newHead.data = headA.data;
            newHead.next = mergeLists(headA.next, headB);
        }
        else {
            newHead.data = headB.data;
            newHead.next = mergeLists(headA, headB.next);
        }
        return newHead;
    }

}
