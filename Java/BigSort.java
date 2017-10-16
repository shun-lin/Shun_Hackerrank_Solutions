import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] unsorted = new String[n];
        for(int unsorted_i=0; unsorted_i < n; unsorted_i++){
            unsorted[unsorted_i] = in.next();
        }
        // your code goes here
        Comparator<String> comparator = new Comparator<String>() {

            @Override
            public int compare(String s1, String s2) {
                if (s1.length() > s2.length()) {
                    return 1;
                }
                else if (s1.length() < s2.length()) {
                    return -1;
                }
                else {
                    return s1.compareTo(s2);
                }
            }
        };

        Arrays.sort(unsorted, comparator);
        for (String sorted : unsorted) {
            System.out.println(sorted);
        }
    }
}
