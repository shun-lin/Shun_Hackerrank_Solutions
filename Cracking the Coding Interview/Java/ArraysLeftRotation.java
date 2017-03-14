import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        int index;
        for (int i = 0; i < n; i += 1) {
            index = i + k;
            if (index >= n) {
                index -= n;
            }
            System.out.print(a[index]);
            System.out.print(" ");
        }
    }
}
