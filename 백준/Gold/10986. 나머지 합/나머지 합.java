
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

//11660. 구간 합 구하기 5
public class Main {
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        //n-m까지의 합
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        Map<Integer, Integer> curSum = new HashMap<>();

        int[] data = new int[n + 1];

        st = new StringTokenizer(br.readLine());

        //각 누적합 별로 카운트
        for (int i = 1; i < n + 1; i++) {
            data[i] = (Integer.parseInt(st.nextToken())%m + data[i - 1]%m) % m;
            curSum.putIfAbsent(data[i], 0);
            curSum.put(data[i], curSum.get(data[i]) + 1);
        }
        
        long result = 0;
        for (int key : curSum.keySet()) {
            long size = curSum.get(key);
            result += size * (size - 1) / 2;

            if (key == 0) {
                result += size;
            }
        }
        System.out.println(result);
    }
}
