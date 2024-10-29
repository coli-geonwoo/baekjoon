import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {


    private static int n;
    private static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        nums = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken()) % 7;
        }

        boolean[] dp = new boolean[7];
        dp[0] = true;

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            List<Integer> temp = new ArrayList<>();
            for (int j = 0; j < 7; j++) {
                if (dp[j]) {
                    temp.add((j + num) % 7);
                }
            }

            for (int idx : temp) {
                dp[idx] = true;
            }

            dp[num] = true;

            if (dp[4]) {
                break;
            }
        }

        if (dp[4]) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
