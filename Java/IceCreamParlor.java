import java.io.*;
import java.util.*;

public class Solution {

    public static int[] ids(int m, int n, int[] costs) {
        // this hashmap has the money needed as key and the id as value
        HashMap<Integer, Integer> hashmap = new HashMap<Integer, Integer>();

        int[] result = new int[2];
        for (int i = 0; i < n; i += 1) {
            int cost_i = costs[i];
            if (hashmap.containsKey(cost_i)) {
                int index_other = hashmap.get(cost_i);
                result[0] = index_other + 1;
                result[1] = i + 1;
                return result;
            }
            int money_needed = m - cost_i;
            hashmap.put(money_needed, i);
        }
        return result;
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int num_cases = in.nextInt();
        for (int num_case = 0; num_case < num_cases; num_case += 1) {
            int m = in.nextInt();
            int n = in.nextInt();
            int[] costs = new int[n];
            for(int i = 0; i < n; i += 1){
                costs[i] = in.nextInt();
            }
            int[] result = ids(m, n, costs);
            System.out.print(result[0]);
            System.out.print(" ");
            System.out.println(result[1]);
        }
    }

}
