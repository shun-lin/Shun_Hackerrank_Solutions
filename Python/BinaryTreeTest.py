""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    if (root == None):
        return True;
    if (root.left == None and root.right == None):
        return True;
    elif (root.left == None):
        if (root.right.data > root.data):
            return check_binary_search_tree_(root.right);
        else:
            return False;
    elif (root.right == None):
        if (root.left.data < root.data):
            return check_binary_search_tree_(root.left);
        else:
            return False;
    else:
        if (root.left.data < root.data and root.right.data > root.data):
            answer = check_binary_search_tree_(root.right);
            if (answer == True):
                return check_binary_search_tree_(root.left);
            else:
                return False;
        else:
            return False;
