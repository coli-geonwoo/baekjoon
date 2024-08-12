
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static int count;
    static char[][] data;
    static boolean[][] visited;
    static int result;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        count = Integer.parseInt(st.nextToken());

        data = new char[n][m];
        visited = new boolean[n][m];
        result = 0;

        for (int i = 0; i < n; i++) {
            char[] temp = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                data[i][j] = temp[j];
            }
        }

        visited[n - 1][0] = true;
        dfs(n - 1, 0, 1);
        System.out.println(result);
    }

    static void dfs(int x, int y, int cnt) {

        if (cnt == count && x == 0 && y == m - 1) {
            result += 1;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m || data[nx][ny] == 'T' || visited[nx][ny]) {
                continue;
            }

            visited[nx][ny] = true;
            dfs(nx, ny, cnt + 1);
            visited[nx][ny] = false;
        }
    }
}

