import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    // return the highest index
    static int highest(int sum_height_h1, int sum_height_h2, int sum_height_h3) {
        if (sum_height_h1 >= sum_height_h2 && sum_height_h1 >= sum_height_h3) {
            return 1;
        }
        else if (sum_height_h2 >= sum_height_h3 && sum_height_h2 >= sum_height_h1) {
            return 2;
        }
        else {
            return 3;
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n1 = in.nextInt();
        int n2 = in.nextInt();
        int n3 = in.nextInt();
        int h1[] = new int[n1];
        int sum_height_h1 = 0;
        for(int h1_i=0; h1_i < n1; h1_i++){
            h1[h1_i] = in.nextInt();
            sum_height_h1 += h1[h1_i];
        }
        int h2[] = new int[n2];
        int sum_height_h2 = 0;
        for(int h2_i=0; h2_i < n2; h2_i++){
            h2[h2_i] = in.nextInt();
            sum_height_h2 += h2[h2_i];
        }
        int h3[] = new int[n3];
        int sum_height_h3 = 0;
        for(int h3_i=0; h3_i < n3; h3_i++){
            h3[h3_i] = in.nextInt();
            sum_height_h3 += h3[h3_i];
        }
        int last_index1 = 0;
        int last_index2 = 0;
        int last_index3 = 0;
        while (!(sum_height_h1 == sum_height_h2 && sum_height_h2 == sum_height_h3)) {
            int highest_stack = highest(sum_height_h1, sum_height_h2, sum_height_h3);
            if (highest_stack == 1) {
                sum_height_h1 -= h1[last_index1];
                last_index1 += 1;
            }
            else if (highest_stack == 2) {
                sum_height_h2 -= h2[last_index2];
                last_index2 += 1;
            }
            else {
                sum_height_h3 -= h3[last_index3];
                last_index3 += 1;
            }
        }
        System.out.println(sum_height_h1);
    }
}
