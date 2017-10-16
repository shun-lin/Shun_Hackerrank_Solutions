/*
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;

*/

void decode(String S ,Node root)
    {
        // error checking
        if (S == null || S.length() == 0 || root == null) {
            return;
        }

        StringBuilder builder = new StringBuilder();

        Node temp = root;
        int i = 0;
        while (i < S.length()) {
            // should go left
            if (S.charAt(i) == '0') {
                if (temp.left == null) {
                    builder.append(temp.data);
                    temp = root;
                }
                else {
                    temp = temp.left;
                    i += 1;
                }
            }
            // should go right
            else  {
                if (temp.right == null) {
                    builder.append(temp.data);
                    temp = root;
                }
                else {
                    temp = temp.right;
                    i += 1;
                }
            }
        }
        builder.append(temp.data);
        System.out.println(builder.toString());
    }
