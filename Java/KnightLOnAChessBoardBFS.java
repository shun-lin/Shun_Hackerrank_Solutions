import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import javafx.util.Pair;

public class Solution {

    public static List<Pair<Integer, Integer>> possibleNextMoves(int a, int b) {
        List<Pair<Integer, Integer>> result = new ArrayList<Pair<Integer, Integer>>();
        Pair<Integer, Integer> leftUp = new Pair<Integer, Integer>(-a, b);
        result.add(leftUp);
        Pair<Integer, Integer> upLeft = new Pair<Integer, Integer>(-b, a);
        result.add(upLeft);
        Pair<Integer, Integer> leftDown = new Pair<Integer, Integer>(-a, -b);
        result.add(upLeft);
        Pair<Integer, Integer> downLeft = new Pair<Integer, Integer>(-b, -a);
        result.add(downLeft);
        Pair<Integer, Integer> rightUp = new Pair<Integer, Integer>(a, b);
        result.add(rightUp);
        Pair<Integer, Integer> upRight = new Pair<Integer, Integer>(b, a);
        result.add(upRight);
        Pair<Integer, Integer> rightDown = new Pair<Integer, Integer>(a, -b);
        result.add(rightDown);
        Pair<Integer, Integer> downRight = new Pair<Integer, Integer>(b, -a);
        result.add(downRight);

        return result;
    }

    // perform a breadth first search on the graph, starting position is (0, 0)
    public static int minStepToGoal(int a, int b, int n) {
        HashSet<Pair<Integer, Integer>> visited = new HashSet<Pair<Integer, Integer>>();
        // the key is a list of [a, b, steps]
        Queue<List<Integer>> fringe = new LinkedList<List<Integer>>();
        List<Integer> origin = new ArrayList<Integer>();
        origin.add(0);
        origin.add(0);
        origin.add(0);
        fringe.add(origin);

        List<Pair<Integer, Integer>> possibleMoves = possibleNextMoves(a, b);

        while (!fringe.isEmpty()) {
            List<Integer> toVisit = fringe.remove();
            int x = toVisit.get(0);
            int y = toVisit.get(1);
            int steps = toVisit.get(2);
            Pair<Integer, Integer> key = new Pair(x, y);
            visited.add(key);
            // we found the steps
            if (x == n - 1 && y == n - 1) {
                return steps;
            }
            // explore all possible next steps
            for (Pair<Integer, Integer> possibleMove : possibleMoves) {
                int dx = possibleMove.getKey();
                int dy = possibleMove.getValue();

                int newX = x + dx;
                int newY = y + dy;

                // out of bound
                if (newX < 0 || newY < 0 || newX > n - 1 || newY > n - 1) {
                    continue;
                }

                Pair<Integer, Integer> child_key = new Pair<Integer, Integer>(newX, newY);
                // we visited this before
                if (visited.contains(child_key)) {
                    continue;
                }

                // add this to fringe
                int newSteps = steps + 1;
                List<Integer> toAdd = new ArrayList<Integer>();
                toAdd.add(newX);
                toAdd.add(newY);
                toAdd.add(newSteps);

                fringe.add(toAdd);

            }
        }
        // can't find a path
        return -1;
    }

    public static int[][] knights(int n) {
        int[][] result = new int[n - 1][n - 1];
        HashMap<Pair<Integer, Integer>, Integer> hashmap = new HashMap<Pair<Integer, Integer>, Integer>();

        for (int i = 0; i < n - 1; i += 1) {
            for (int j = 0; j < n - 1; j += 1) {
                int a = i + 1;
                int b = j + 1;
                int minStep = 0;
                Pair<Integer, Integer> key = new Pair<Integer, Integer>(a, b);
                // already calculated this pair
                if (hashmap.containsKey(key)) {
                    minStep = hashmap.get(key);
                }
                else {
                    minStep = minStepToGoal(a, b, n);
                    // put the other key (b, a) in hashmap
                    Pair<Integer, Integer> other_key = new Pair<Integer, Integer>(b, a);
                    hashmap.put(key, minStep);
                    result[i][j] = minStep;
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[][] result = knights(n);
        for (int[] row : result) {
            System.out.print(row[0]);
            for (int i = 1; i < row.length; i += 1) {
                System.out.print(" " + Integer.toString(row[i]));
            }
            System.out.println();
        }
    }
}
