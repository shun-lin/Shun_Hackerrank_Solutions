

 /* Node is defined as :
 class Node
    int data;
    Node left;
    Node right;

    */

static Node lca(Node root,int v1,int v2)
    {
        if (root == null) {
            return new Node();
        }
        else if (root.data > v1 && root.data > v2) {
            return lca(root.left, v1, v2);
        }
        else if (root.data < v1 && root.data < v2) {
            return lca(root.right, v1, v2);
        }
        else {
            return root;
        }
    }
