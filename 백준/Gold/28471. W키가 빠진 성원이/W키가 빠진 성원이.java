import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

//28471. W키가 빠진 성원이
public class Main {
    static int result = 0;
    static char [][] data;
    static Deque<Node> q = new ArrayDeque<>();
    static int n;
    static int [] dx = {-1, -1, 0, 0, 1, -1, 1};
    static int [] dy= {-1, 1, -1, 1, -1, 0 ,1};



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int [][] visited = new int [n][n];
        data = new char[n][n];
        int sx=0;
        int sy=0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            char [] s = st.nextToken().toCharArray();
            for (int j = 0; j < n; j++) {
                data[i][j] = s[j];
                if (data[i][j] == 'F'){
                    sx=i;
                    sy=j;
                }
            }
        }

        q.add(new Node(sx, sy));
        visited[sx][sy]=1;

        while(!q.isEmpty()){
            Node cur = q.pollFirst();

            for (int i = 0; i < 7; i++) {
                int nx = cur.x+dx[i];
                int ny = cur.y+dy[i];

                if(nx<0 || nx>=n || ny<0 || ny>=n || visited[nx][ny]==1 || data[nx][ny] == '#'){
                    continue;
                }
                visited[nx][ny]=1;
                result++;
                q.add(new Node(nx, ny));
            }
        }

//        for (int i = 0; i < n; i++) {
//            for (int j = 0; j < n; j++) {
//                System.out.print(visited[i][j] + " ");
//            }
//            System.out.println();
//        }

        System.out.println(result);

    }

    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

}

