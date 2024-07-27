import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//26259. 백룸(골4)
public class Main {
    static int dist = -1; //가로 : 0 세로 :1
    static long[][] dp;
    static long[][] data;
    static int n;
    static int m;
    static int wx1, wy1, wx2, wy2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new long[n][m];
        dp = new long[n + 1][m + 1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 벽 가로-새로 판단
        st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        if ((a == c && b < d) || (b == d && a < c)) {
            wx1 = a;
            wy1 = b;
            wx2 = c;
            wy2 = d;
        } else {
            wx1 = c;
            wy1 = d;
            wx2 = a;
            wy2 = b;
        }

        if (wx1 == wx2 && wy1 == wy2) {
        } else if (wx1 == wx2) {
            dist = 0; //가로
        } else {
            dist = 1; //세로
        }
        dp[1][1] = data[0][0];

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {

                if (i == 1 && j == 1) {
                    continue;
                }

                long top = i - 1 == 0 ? -Integer.MAX_VALUE : dp[i - 1][j];
                long left = j - 1 == 0 ? -Integer.MAX_VALUE : dp[i][j - 1];

                if (dist == 0 && (i - 1) == wx1 && (j - 1) >= wy1 && (j - 1) < wy2) {
                    top = -Integer.MAX_VALUE;
                } else if (dist == 1 && (j - 1) == wy1 && (i - 1) >= wx1 && (i - 1) < wx2) {
                    left = -Integer.MAX_VALUE;
                }

                if (top == -Integer.MAX_VALUE && left == -Integer.MAX_VALUE) {
                    dp[i][j] = -Integer.MAX_VALUE;
                } else {
                    dp[i][j] = Math.max(top, left) + data[i - 1][j - 1];
                }
            }
        }
//
//        for (int i = 1; i < n + 1; i++) {
//            for (int j = 1; j < m + 1; j++) {
//                System.out.print(dp[i][j] + " ");
//            }
//            System.out.println();
//
//        }

        if (dp[n][m] == - Integer.MAX_VALUE) {
            System.out.println("Entity");
        } else {
            System.out.println(dp[n][m]);
        }
    }

}

