
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int holeCnt;
    static int weight;
    static int[] nums;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        holeCnt = Integer.parseInt(s[0]);
        weight = Integer.parseInt(s[1]);
        StringTokenizer st = new StringTokenizer(br.readLine());
        nums = new int[holeCnt + 1];
        for (int i = 1; i < holeCnt + 1; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int temp = 0;
        int result = 0;

        while (true) {
            if (temp <= weight) {
                result = Math.max(result, temp);
                if (right == holeCnt) {
                    break;
                }
                temp += nums[++right];
            } else {
                if (left == holeCnt) {
                    break;
                }
                temp -= nums[left++];
            }
        }

        System.out.println(result);
    }


}