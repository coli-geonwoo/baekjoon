import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int k;
    static int [] nums;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        k = Integer.parseInt(s[1]);

        nums = new int[2*n-1];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            nums[i]= Integer.parseInt(st.nextToken());
        }

        for(int i=n; i<2*n-1; i++){
            nums[i] = nums[i-n];
        }

        int result =0;
        int temp=0;

        for(int i=0; i<k; i++){
            temp+=nums[i];
        }
        result= temp;

        for(int i=k; i<2*n-1; i++){
            temp = temp + nums[i]-nums[i-k];
            result = Math.max(result, temp);
        }

        System.out.println(result);
    }
}