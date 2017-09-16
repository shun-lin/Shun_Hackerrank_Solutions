'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if (root == None):
        return 0;
    if (root.left == None and root.right == None):
        return 0;
    left_height = height(root.left);
    right_height = height(root.right);
    return max(left_height, right_height) + 1;
