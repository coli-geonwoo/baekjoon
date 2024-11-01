
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;
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

        Deque<Integer> window = new ArrayDeque<>();
        int result = Integer.MAX_VALUE;

        for (int i = 0; i < k; i++) {
            window.add(numbers[i]);
            result = Math.min(result, numbers[i]);
        }
        int temp = result;
        
        for (int i = k; i < n; i++) {
            int poll = window.pollFirst();
            window.add(numbers[i]);
//            temp = Math.min(temp, numbers[i]);
            if (result < numbers[i] && poll <= result) {
                result = Math.max(result, Collections.min(window));
            }
        }

        System.out.println(result);
    }
}
