import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static long n;
    static long k;
    static long[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Long.parseLong(st.nextToken());
        k = Long.parseLong(st.nextToken());
        nums = new long[(int) n];

        //불꽃 놀이 받기
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            nums[i]= Long.parseLong(st.nextToken());
        }

        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;

        int cnt = 0;

        while(right>=0 && nums[right]>=k){
            cnt++;
            right--;
        }

        while(left<right){
            long temp = nums[left]+ nums[right];
            if(temp<k){
                left++;
            }else{
                cnt++;
                left++;
                right--;
            }
        }

        if (cnt != 0) {
            System.out.println(cnt);
        } else {
            System.out.println(-1);
        }
    }

}
