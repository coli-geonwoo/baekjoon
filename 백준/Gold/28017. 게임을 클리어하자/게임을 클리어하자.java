
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static int playCnt;
    static int weaponCnt;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        playCnt = Integer.parseInt(s[0]);
        weaponCnt = Integer.parseInt(s[1]);
        dp = new int[playCnt + 1][weaponCnt];
        int[][] data = new int[playCnt + 1][weaponCnt];

        for (int i = 1; i < playCnt + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < weaponCnt; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i <= playCnt; i++) {
            for (int j = 0; j < weaponCnt; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = 0; k < weaponCnt; k++) {
                    if (j == k) {
                        continue;
                    }
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][k] + data[i][k]);
                }
            }
        }

        int result = Integer.MAX_VALUE;

        for (int i = 0; i < weaponCnt; i++) {
            result = Math.min(result, dp[playCnt][i]);
        }

        System.out.println(result);
    }

}