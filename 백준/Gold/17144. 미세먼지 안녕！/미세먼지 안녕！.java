
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static int n;
    private static int m;
    private static int chengjunggi1;
    private static int chengjunggi2;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};


    //17144. 미세먼지 안녕
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        int t = Integer.parseInt(s[2]);


        int[][] data = new int[n][m];
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            String[] d = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                data[i][j] = Integer.parseInt(d[j]);
                if (data[i][j] == -1) {
                    if (flag) {
                        chengjunggi1 = i;
                        flag = false;
                    } else {
                        chengjunggi2 = i;
                    }
                }

            }
        }

        for (int i = 0; i < t; i++) {
            data= misemeonji(data);
            data = blow_up(data);
            data = blow_down(data);
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (data[i][j] != -1) {
                    result += data[i][j];
                }
            }
        }

        System.out.println(result);
    }

    private static int[][] misemeonji(int[][] data) {
        int[][] temp = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                temp[i][j] = data[i][j];
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (data[i][j] > 0) {
                    int cnt = 0;
                    for (int k = 0; k < 4; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];

                        if (nx < 0 || ny < 0 || nx >= n || ny >= m || data[nx][ny] == -1) {
                            continue;
                        }
                        temp[nx][ny] += data[i][j] / 5;
                        cnt++;
                    }
                    temp[i][j] -= (data[i][j] / 5) * cnt;
                }
            }
        }
        return temp;
    }

    private static int[][] blow_up(int[][] data) {
        int[][] temp = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                temp[i][j] = data[i][j];
            }
        }

        for (int i = 1; i < m; i++) {
            temp[0][i - 1] = data[0][i];
            temp[chengjunggi1][i] = data[chengjunggi1][i - 1];
        }
        temp[chengjunggi1][1] = 0;

        for (int i = 1; i < chengjunggi1+1; i++) {
            temp[i][0] = data[i - 1][0];
            temp[chengjunggi1-i][m - 1] = data[chengjunggi1+1-i][m - 1];
        }
        temp[chengjunggi1][0] = -1;

        return temp;
    }

    private static int[][] blow_down(int[][] data) {
        int[][] temp = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                temp[i][j] = data[i][j];
            }
        }

        for (int i = 1; i < m; i++) {
            temp[n - 1][i - 1] = data[n - 1][i];
            temp[chengjunggi2][i] = data[chengjunggi2][i - 1];
        }
        temp[chengjunggi2][1] = 0;

        for (int i = chengjunggi2 + 1; i < n; i++) {
            temp[i - 1][0] = data[i][0];
            temp[i][m - 1] = data[i - 1][m - 1];
        }
        temp[chengjunggi2][0] = -1;

        return temp;
    }
}
