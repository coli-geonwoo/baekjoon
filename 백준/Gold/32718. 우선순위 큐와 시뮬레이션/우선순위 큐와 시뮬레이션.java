
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int[] nums;
    static int n;
    static int k;
    static int t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 모든 원소에 대해 Ai를 더한다.
        // k로 나는 나머지를 취한다.
        // top을 출력한다

        n = Integer.parseInt(st.nextToken()); // 총 원소의 개수
        k = Integer.parseInt(st.nextToken()); // 나누는 수
        t = Integer.parseInt(st.nextToken()); // 쿼리 개수

        nums = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken()) % k;
        }
        Arrays.sort(nums);

        //턴 진행하기
        st = new StringTokenizer(br.readLine());
        int addNum = 0;

        for (int i = 0; i < t; i++) {
            addNum += Integer.parseInt(st.nextToken());
            addNum%=k;
            int result = turn(addNum);
            bw.write(result + " ");
        }

        bw.flush();
    }

    public static int turn(int addNum) {
        // 1 2 3 4 5 -> addNum 3 bound 2
        // 4 5
        int bound = k - addNum; //bound와 같은 값까지 bisect_left
        int left = 0;
        int right = n - 1;
        int result = -1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int num = nums[mid];

            if (num < bound) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if (result == -1) {
            result = n - 1;
        }
//        System.out.println("result = " + result);
//        System.out.println("addNum = " + addNum);
//        System.out.println(Arrays.toString(nums));
//        System.out.println("===");

        return (nums[result] + addNum) % k;
    }

}
