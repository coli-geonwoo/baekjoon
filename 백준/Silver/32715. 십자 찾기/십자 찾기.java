
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int[][] data;
    static int [][] curSum1;
    static int [][] curSum2;
    static int [] dx = {-1,1,0,0};
    static int [] dy = {0,0,-1,1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(br.readLine());

        data = new int[n][m];
        curSum1 = new int[n+1][m+1];
        curSum2 = new int[n+1][m+1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
                curSum1[i+1][j+1] += curSum1[i+1][j]+ data[i][j];
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                curSum2[j+1][i+1] = curSum2[j][i+1] +data[j][i];
            }
        }

        int cnt =0;
        if(n>=2*k+1 && m>=2*k+1) {
            for (int i = k; i < n - k; i++) {
                for (int j = k; j < m - k; j++) {
                    if (data[i][j] == 1 && isTenShape(i, j, k)) {
                        cnt++;
                    }
                }
            }
        }
//
//        for (int i = 0; i < n+1; i++) {
//            System.out.println(Arrays.toString(curSum1[i]));
//        }
//        System.out.println();
//        for (int i = 0; i < n+1; i++) {
//            System.out.println(Arrays.toString(curSum2[i]));
//        }

        bw.write(String.valueOf(cnt));
        bw.flush();
    }

    private static boolean isTenShape(int x, int y, int k) {
        int right = curSum1[x+1][y+1+k]- curSum1[x+1][y+1];
        int left = curSum1[x+1][y]- curSum1[x+1][y-k];
        int down = curSum2[x][y+1]- curSum2[x-k][y+1];
        int up = curSum2[x+1+k][y+1]- curSum2[x+1][y+1];

        if(right==k && left==k && down==k && up==k) {
            return true;
        }
        return false;
    }
}
