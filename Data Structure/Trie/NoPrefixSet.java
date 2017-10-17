import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static class TrieNode {

        public char data;
        public HashMap<Character, TrieNode> children;
        public boolean endOfWord;

        // use this consturctor for head trie node
        public TrieNode() {
            this.data = ' ';
            this.children = new HashMap<Character, TrieNode>();
            this.endOfWord = false;
        }

        public TrieNode(char c) {
            this.data = c;
            this.children = new HashMap<Character, TrieNode>();
            this.endOfWord = false;
        }

        public char getData() {
            return this.data;
        }

        public void setData(char c) {
            this.data = c;
        }

        public boolean isEndOfWord() {
            return this.endOfWord;
        }

        public void setEndOfWord() {
            this.endOfWord = true;
        }

        public void unsetEndOfWord() {
            this.endOfWord = false;
        }

        // return true if this word does not violate constrain (not a prefix of another word or is another word prefix of this)
        public boolean addWord(String word, int i) {
            if (this.endOfWord) {
                return false;
            }
            if (i == word.length()) {
                if (!this.children.isEmpty()) {
                    return false;
                }
                this.endOfWord = true;
                return true;
            }
            char key = word.charAt(i);
            if (this.children.containsKey(key)) {
                TrieNode childNode = this.children.get(key);
                return childNode.addWord(word, i + 1);
            }
            else {
                TrieNode newNode = new TrieNode(key);
                this.children.put(key, newNode);
                return newNode.addWord(word, i + 1);
            }
        }
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String word = in.nextLine();
        TrieNode head = new TrieNode();
        for (int i = 0; i < n; i += 1) {
            word = in.nextLine();
            int start = 0;
            boolean isGood = head.addWord(word, start);
            if (!isGood) {
                System.out.println("BAD SET");
                System.out.println(word);
                return;
            }

        }
        System.out.println("GOOD SET");
    }
}
