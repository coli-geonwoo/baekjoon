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

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        long[] nums = new long[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        long result = 1;
        int idx =0;

        while(idx<n){
            boolean exeFlag = true;
            int eraseCnt=0;
            long num = nums[idx];

            int tempCnt = 1;
            int tempIdx = idx+1;
            int sameIdx = idx;

            while(tempIdx<n && eraseCnt<=k){
                if(nums[tempIdx] != num){
                    exeFlag = false;
                    tempIdx++;
                    eraseCnt++;
                    continue;
                }
                tempCnt++;
                if(exeFlag) {
                    sameIdx = tempIdx;
                }
                tempIdx++;
            }

            result = Math.max(result, tempCnt);
            idx = sameIdx+1;
        }

        bw.write(String.valueOf(result));
        bw.flush();
    }
}
