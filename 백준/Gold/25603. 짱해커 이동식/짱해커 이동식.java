
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

//25603. 짱해커 이동식(골5)
public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        //데이터 준비
        int[] numbers = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        PriorityQueue<Integer> min_nums = new PriorityQueue<>();
        int idx = 0;

        while (idx + k <= n) {
            int[] window = Arrays.copyOfRange(numbers, idx, idx + k);
            int temp = window[0];
            int temp_idx = idx;
            for (int i = 0; i < window.length; i++) {
                if (temp >= window[i]) {
                    temp_idx = idx + i + 1;
                    temp = window[i];
                }
            }

            min_nums.add(-temp);
            idx = temp_idx;
        }

        System.out.println(-min_nums.peek());
    }
}
