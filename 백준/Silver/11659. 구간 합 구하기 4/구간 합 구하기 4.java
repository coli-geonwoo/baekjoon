
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class Main {
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[] nums = new int[n + 1];

        // 데이터 읽기
        st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= n; i++) {
            nums[i] += nums[i - 1] + Integer.parseInt(st.nextToken());
        }

        StringJoiner sj = new StringJoiner(System.lineSeparator());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int sum = nums[end] - nums[start-1];
            sj.add(String.valueOf(sum));
        }

        System.out.println(sj);
    }
}
