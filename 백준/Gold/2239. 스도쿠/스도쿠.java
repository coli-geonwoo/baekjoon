import static java.lang.System.exit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static int[][] sudoku;
    private static List<Node> nodes = new ArrayList<>();
    private static int blank=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sudoku = new int[9][9];
        for (int i = 0; i < 9; i++) {
            char[] s = br.readLine().toCharArray();
            for (int j = 0; j < 9; j++) {
                int b = Integer.parseInt(String.valueOf(s[j]));
                if (b == 0) {
                    blank++;
                    nodes.add(new Node(i, j));
                }
                sudoku[i][j] = b;
            }
        }

        blank = nodes.size();
//        System.out.println(blank);

        solve(0);


    }

    public static void solve(int index) {
        if (index == blank) {
            shut_down();
        }
        Node cur = nodes.get(index);
        int row = cur.x;
        int col = cur.y;

        for (int i = 1; i <= 9; i++) {
            if (avaliable(row, col, i)) {
                sudoku[row][col] = i;
                solve(index + 1);
                sudoku[row][col] = 0;
            }
        }
    }

    public static void shut_down() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print(sudoku[i][j]);
            }
            if(i!=8) {
                System.out.println();
            }
        }
        exit(0);
    }

    public static boolean avaliable(int row, int col, int value) {
        if (!row(row, value) || !col(col, value) || !square(row, col, value)) {
            return false;
        }
        return true;
    }

    public static boolean row(int row, int value) {
        for (int i = 0; i < 9; i++) {
            if (sudoku[row][i] == value) {
                return false;
            }
        }
        return true;
    }

    public static boolean col(int col, int value) {
        for (int i = 0; i < 9; i++) {
            if (sudoku[i][col] == value) {
                return false;
            }
        }
        return true;
    }

    public static boolean square(int row, int col, int value) {
        for (int i = (row / 3) * 3; i < (row / 3) * 3 + 3; i++) {
            for (int j = (col / 3) * 3; j < (col / 3) * 3 + 3; j++) {
                if (sudoku[i][j] == value) {
                    return false;
                }
            }
        }
        return true;
    }

    static class Node {
        int x;
        int y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
