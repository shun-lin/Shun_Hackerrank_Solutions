/*
Detect a cycle in a linked list. Note that the head pointer may be 'null' if the list is empty.

A Node is defined as:
    class Node {
        int data;
        Node next;
    }
*/

boolean hasCycle(Node head) {
    if (head == null) {
        return false;
    }
    Node slow = head;
    Node fast = head;
    if (slow.next == null) {
        return false;
    }
    slow = slow.next;
    if (slow.next == null) {
        return false;
    }
    fast = slow.next;
    while (fast.next != null && fast.next.next != null) {
        if (slow == fast) {
            return true;
        }
        slow = slow.next;
        fast = fast.next;
        fast = fast.next;
    }
    return false;
}
