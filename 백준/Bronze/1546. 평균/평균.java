
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long max= 0;

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int [] nums = new int[n];


        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            max= Math.max(max, nums[i]);
        }

        double avgSum=0;
        for (int i = 0; i < n; i++) {
            avgSum += (double)nums[i]/max *100;
        }

        System.out.println(avgSum/n);
    }
}
