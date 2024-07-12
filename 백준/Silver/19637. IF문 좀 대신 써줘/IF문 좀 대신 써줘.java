
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static String[] rank;
    static int[] threshold;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        rank = new String[n];
        threshold = new int[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            rank[i] = st.nextToken();
            threshold[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < m; i++) {
            int j = Integer.parseInt(br.readLine());
            System.out.println(solve(j));
        }


    }

    static String solve(int i) {
        int left = 0;
        int right = n - 1;
        String result = "";

        while (left <= right) {
            int mid = (left + right) / 2;
            int k = threshold[mid];
            
            if (i <= k) {
                result = rank[mid];
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }
}