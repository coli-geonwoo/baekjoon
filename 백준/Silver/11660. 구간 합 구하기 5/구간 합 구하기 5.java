
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringJoiner;
import java.util.StringTokenizer;

//11660. 구간 합 구하기 5
public class Main {
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[][] data = new int[n+1][n+1];

        for (int i = 1; i < n+1; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n+1; j++) {
                int k = Integer.parseInt(st.nextToken());
                data[i][j] = data[i-1][j] + data[i][j-1] - data[i-1][j-1] +k;
            }
        }

        StringJoiner sj = new StringJoiner(System.lineSeparator());

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int sx = Integer.parseInt(st.nextToken());
            int sy = Integer.parseInt(st.nextToken());
            int ex = Integer.parseInt(st.nextToken());
            int ey = Integer.parseInt(st.nextToken());
            long result = data[ex][ey] - data[sx-1][ey] - data[ex][sy-1] + data[sx-1][sy-1];

            sj.add(String.valueOf(result));
        }

        System.out.println(sj);
    }
}
