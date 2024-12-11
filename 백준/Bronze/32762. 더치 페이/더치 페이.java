
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

        double result = 0;
        double foodMoney = 0;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            br.readLine();
        }

        for (int i = 0; i < m; i++) {
            String[] split = br.readLine().split(" ");
            foodMoney+=Double.parseDouble(split[1]);
        }

        bw.write(String.valueOf(Math.round(foodMoney*10000/n)/10000.0));
        bw.flush();
        bw.close();
    }
}
