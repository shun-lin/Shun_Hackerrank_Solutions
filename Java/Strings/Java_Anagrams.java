static boolean isAnagram(String a, String b) {
    // Complete the function
    if (a == null || b == null || a.length() != b.length()) {
        return false;
    }
    else {
        a = a.toLowerCase();
        b = b.toLowerCase();
        int[] result = new int[26];
        for (int i = 0; i < a.length(); i += 1) {
            char aChar = a.charAt(i);
            int aIndex = aChar - 'a';
            char bChar = b.charAt(i);
            int bIndex = bChar - 'a';
            result[aIndex] += 1;
            result[bIndex] -= 1;
        }
        for (int charCount : result) {
            if (charCount != 0) {
                return false;
            }
        }
        return true;
    }
}
