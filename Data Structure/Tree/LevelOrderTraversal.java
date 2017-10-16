/*

 class Node
    int data;
    Node left;
    Node right;
*/

// breath first search
void levelOrder(Node root) {
    if (root == null) {
        return;
    }
    boolean isFirst = true;
    Queue<Node> queue = new LinkedList<Node>();
    queue.add(root);
    while (!queue.isEmpty()) {
        Node visiting = queue.remove();
        if (isFirst) {
            isFirst = false;
            System.out.print(visiting.data);
        }
        else {
            System.out.print(" ");
            System.out.print(visiting.data);
        }
        if (visiting.left != null) {
            queue.add(visiting.left);
        }
        if (visiting.right != null) {
            queue.add(visiting.right);
        }
    }

 }
