""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import math;

def check_binary_search_tree_(root):
    def check_helper(root, lower_bound, upper_bound):
        if not root:
            return True;
        else:
            if root.data <= lower_bound or root.data >= upper_bound:
                return False;
            elif root.left and root.left.data >= root.data:
                return False;
            elif root.right and root.right.data <= root.data:
                return False;
            else:
                return check_helper(root.left, lower_bound, root.data) and check_helper(root.right, root.data, upper_bound);
    return check_helper(root, -math.inf, math.inf);
