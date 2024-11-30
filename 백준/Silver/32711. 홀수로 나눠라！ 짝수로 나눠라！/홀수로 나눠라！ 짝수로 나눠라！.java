
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        //전체 합
        long total = 0;
        long curSum = 0;
        int evenCnt = 0;
        int n = Integer.parseInt(br.readLine());
        long [] nums = new long[n];

        st= new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
            total += nums[i];
            curSum += nums[i];
            if(i!=n-1 && curSum%2==0){
                evenCnt++;
            }
        }

        //홀수
        boolean flag = false;
        if(total%2!=0){
            flag=true;
        }else if(evenCnt>0){
            flag=true;
        }

        if(flag){
            System.out.println(1);
        }else{
            System.out.println(0);
        }
    }
}

