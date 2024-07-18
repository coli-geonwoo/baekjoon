
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//16401
public class Main {
    static char[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        arr = br.readLine().toCharArray();
        int[] dp = new int[arr.length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 1;

        if (isBig(arr[0])) {
            dp[0]++;
        }

        for (int i = 1; i < arr.length; i++) {
            char c = arr[i];

            if (isDifferent(c, arr[i - 1])) {
                dp[i] = Math.min(dp[i], dp[i - 1] + 2);
            } else {
                dp[i] = Math.min(dp[i], dp[i - 1] + 1);
            }

            if (i >= 2
                    && !isDifferent(c, arr[i - 2])
                    && isDifferent(c, arr[i-1])
            ) {
                dp[i] = Math.min(dp[i], dp[i - 2] + 3);
            }

            if(i==1){
                dp[i]= Math.min(dp[i], 3);
            }
        }

//        for (int i = 0; i < dp.length; i++) {
//            System.out.print(dp[i] + " ");
//        }
//        System.out.println();

        System.out.println(dp[dp.length - 1]);
    }

    private static boolean isBig(char c) {
        return c >= 'A' && c <= 'Z';
    }

    private static boolean isDifferent(char a, char b) {
        return isBig(a) && !isBig(b) || !isBig(a) && isBig(b);
    }
}