/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.

The Node class is defined as follows:
    class Node {
        int data;
        Node left;
        Node right;
     }
*/
    // a helper function
    static boolean checkBSThelper(Node root, int maximum, int minimum) {
        if (root == null) {
            return true;
        }
        if (root.data >= maximum || root.data <= minimum) {
            return false;
        }
        int left_max = java.lang.Math.min(root.data, maximum);
        int right_min = java.lang.Math.max(root.data, minimum);
        return checkBSThelper(root.left, left_max, minimum) && checkBSThelper(root.right, maximum, right_min);
    };

    boolean checkBST(Node root) {
        if (root == null) {
            return true;
        }

        return checkBSThelper(root, Integer.MAX_VALUE, Integer.MIN_VALUE);
    }
