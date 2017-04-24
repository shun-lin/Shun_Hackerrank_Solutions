"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    #Write your code here
    if (root == None):
        return;
    if (root.left):
        inOrder(root.left);
    print(root.data, end=" ");
    if (root.right):
        inOrder(root.right);
