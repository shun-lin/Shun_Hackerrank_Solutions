"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head:
        return False;
    else:
        head_one = head;
        head_two = head.next;
        while (not head_one is head_two):
            if (head_two == None or head_one == None):
                return False;
            else:
                head_one = head_one.next;
                head_two = head_two.next;
                if head_two == None:
                    return False;
                else:
                    head_two = head_two.next;
        return True;
