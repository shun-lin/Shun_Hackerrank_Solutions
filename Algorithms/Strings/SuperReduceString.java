import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static String super_reduced_string(String s){
        // Complete this function
        List<Character> string_in_list = new ArrayList<Character>();

        // turn the string s into an arraylist of characters
        for (int i = 0; i < s.length(); i += 1) {
            string_in_list.add(s.charAt(i));
        }

        boolean completed = false;

        while (!completed) {
            // loop over the string_in_list to delete adjacent character that are the same
            completed = true;
            for (int i = 0; i < string_in_list.size() - 1; i += 1) {
                if (string_in_list.get(i) == string_in_list.get(i + 1)) {
                    string_in_list.remove(i);
                    string_in_list.remove(i);
                    completed = false;
                }
            }
        }

        // empty string
        if (string_in_list.size() == 0) {
            return "Empty String";
        }

        // turn string_in_list back into a string
        StringBuilder builder = new StringBuilder(string_in_list.size());
        for (Character c : string_in_list) {
            builder.append(c);
        }

        return builder.toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        String result = super_reduced_string(s);
        System.out.println(result);
    }
}
