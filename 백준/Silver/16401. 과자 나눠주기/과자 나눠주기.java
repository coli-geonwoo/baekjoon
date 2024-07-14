import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

//16401
public class Main {
    static PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
    static int snackCnt;
    static int person;
    static int[] snack;
    //과자가 있을 때와 없을 때


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String []s = br.readLine().split(" ");
        person = Integer.parseInt(s[0]);
        snackCnt = Integer.parseInt(s[1]);

        StringTokenizer st = new StringTokenizer(br.readLine());
        snack = new int[snackCnt];

        for (int i = 0; i < snackCnt; i++) {
            snack[i]= Integer.parseInt(st.nextToken());
        }

        Arrays.sort(snack);

        long left = 1;
        long right = 1000000000;
        long result =0;

        while(left<=right){
            long mid = (left+right)/2;
            long tempCnt=0;
       
            for (int i = 0; i < snackCnt; i++) {
                tempCnt += snack[i]/mid;
                if(tempCnt >= person){
                    break;
                }
            }

            if(tempCnt>=person){
                result= mid;
                left= mid+1;
            }else{
                right= mid-1;
            }
        }

        System.out.println(result);
    }
}