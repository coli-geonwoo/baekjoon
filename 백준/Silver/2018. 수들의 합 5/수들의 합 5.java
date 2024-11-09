
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//11660. 구간 합 구하기 5
public class Main {
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        //n-m까지의 합
        n = Integer.parseInt(st.nextToken());
        int[] nums = new int[n];

        for (int i = 1; i < n; i++) {
            nums[i] = nums[i-1] + i; //누적합
        }

        int left = 0;
        int right = 0;
        int temp;
        int result = 1;

        while (left <= right && left < n && right < n) {
            temp = nums[right]- nums[left];
            if (temp == n) {
                result++;
            }
            
            if (temp <= n) {
                right++;
                continue;
            }
            left++;
        }

        System.out.println(result);
    }
}
