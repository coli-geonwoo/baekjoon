
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int [][] dp1 = new int [n][m];
        int [][] dp2 = new int [n][m];
        int [][] dp3 = new int [n][m];
        int [][] dp4 = new int [n][m];

        int [][] nums = new int [n][m];

        //nums 입력받기
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                nums[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int result = nums[0][0];

        //첫번째 가로행 초기화
        dp1[0][0] = nums[0][0];
        result = Math.max(result, dp1[0][0]);

        dp2[0][m-1] = nums[0][m-1];
        result = Math.max(result, dp2[0][m-1]);

        dp3[n-1][0] = nums[n-1][0];
        result = Math.max(result, dp3[n-1][0]);

        dp4[n-1][m-1] = nums[n-1][m-1];
        result = Math.max(result, dp4[n-1][m-1]);

        for (int i = 1; i < m; i++) {
            dp1[0][i] = Math.max(dp1[0][i-1] + nums[0][i], nums[0][i]);
            result = Math.max(result, dp1[0][i]);

            dp2[0][m-1-i] = Math.max(dp2[0][m-i] + nums[0][m-1-i], nums[0][m-1-i]);
            result = Math.max(result, dp2[0][m-1-i]);

            dp3[n-1][i] = Math.max(dp3[n-1][i-1] + nums[n-1][i], nums[n-1][i]);
            result = Math.max(result, dp3[n-1][i]);

            dp4[n-1][m-1-i] = Math.max(dp4[n-1][m-i] + nums[n-1][m-1-i], nums[n-1][m-1-i]);
            result = Math.max(result, dp4[n-1][m-1-i]);
        }

        //첫번째 세로행 초기화
        for (int i = 1; i < n; i++) {
            dp1[i][0] = Math.max(dp1[i-1][0] + nums[i][0], nums[i][0]);
            result = Math.max(result, dp1[i][0]);

            dp2[i][m-1] = Math.max(dp2[i-1][m-1] + nums[i][m-1], nums[i][m-1]);
            result = Math.max(result, dp2[i][m-1]);

            dp3[n-1-i][0] = Math.max(dp3[n-i][0] + nums[n-1-i][0], nums[n-1-i][0]);
            result = Math.max(result, dp3[n-1-i][0]);

            dp4[n-1-i][m-1] = Math.max(dp4[n-i][m-1] + nums[n-1-i][m-1], nums[n-1-i][m-1]);
            result = Math.max(result, dp4[n-1-i][m-1]);
        }

        for (int i = 1; i <n ; i++) {
            for (int j = 1; j < m; j++) {
                int beforeNode1 = Math.max(dp1[i-1][j], dp1[i][j-1]) + nums[i][j];
                dp1[i][j] = Math.max(beforeNode1, nums[i][j]);
                result = Math.max(result, dp1[i][j]);

                int beforeNode2 = Math.max(dp2[i-1][m-1-j], dp2[i][m-j]) + nums[i][m-1-j];
                dp2[i][m-1-j] = Math.max(beforeNode2, nums[i][m-1-j]);
                result = Math.max(result, dp2[i][m-1-j]);

                int beforeNode3 = Math.max(dp3[n-i][j], dp3[n-1-i][j-1]) + nums[n-1-i][j];
                dp3[n-1-i][j] = Math.max(beforeNode3, nums[n-1-i][j]);
                result = Math.max(result, dp3[n-1-i][j]);

                int beforeNode4 = Math.max(dp4[n-i][m-1-j], dp4[n-1-i][m-j]) + nums[n-1-i][m-1-j];
                dp4[n-1-i][m-1-j] = Math.max(beforeNode4, nums[n-1-i][m-1-j]);
                result = Math.max(result, dp4[n-1-i][m-1-j]);
            }
        }
//
//        for (int i = 0; i < n; i++) {
//            System.out.println(Arrays.toString(dp1[i]));
//        }
//        System.out.println();
//        for (int i = 0; i < n; i++) {
//            System.out.println(Arrays.toString(dp2[i]));
//        }
//        System.out.println();
//        for (int i = 0; i < n; i++) {
//            System.out.println(Arrays.toString(dp3[i]));
//        }
//        System.out.println();
//        for (int i = 0; i < n; i++) {
//            System.out.println(Arrays.toString(dp4[i]));
//        }
        bw.write(String.valueOf(result));
        bw.flush();
    }

}
