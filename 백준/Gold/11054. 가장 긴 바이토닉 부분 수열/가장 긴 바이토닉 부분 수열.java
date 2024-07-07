
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    static int[] lis;
    static int[] lds;
    static int[] nums;
    static int n;

    //9466. 텀 프로젝트
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        nums = new int[n];
        lis = new int[n];
        lds = new int[n];

        int idx = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            nums[idx++] = Integer.parseInt(st.nextToken());
        }

        calLis();
        calLds();
        int result = 0;

        for(int i=0; i<n; i++){
//            System.out.println("lis : "+ lis[i] + " lds : "+ lds[i]);
            result = Math.max(result, lis[i]+ lds[i]);
        }
        System.out.println(result+1);

    }

    private static void calLis() {
        for(int i=0; i<n; i++){
            for(int j=0; j<i; j++){
                if(nums[i] > nums[j]){
                    lis[i] = Math.max(lis[i], lis[j]+1);
                }
            }
        }
    }

    private static void calLds() {
        for(int i=n-1; i>=0; i--){
            for(int j=n-1; j>i; j--){
                if(nums[i] > nums[j]){
                    lds[i] = Math.max(lds[i], lds[j]+1);
                }
            }
        }
    }

}
