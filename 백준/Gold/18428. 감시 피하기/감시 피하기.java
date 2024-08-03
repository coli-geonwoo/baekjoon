

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

//25712. 인경강
public class Main {
    private static int n;
    private static char[][] data;
    private static List<Node> teachers = new ArrayList<>();
    private static List<Node> fields= new ArrayList<>();
    private static int[] fieldVisited;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    private static boolean flag;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);

        data= new char[n][n];

        for (int i = 0; i < n; i++) {
            String [] row = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                data[i][j] = row[j].charAt(0);
                if (data[i][j] == 'T') {
                    teachers.add(new Node(i, j));
                }

                if (data[i][j]  == 'X') {
                    fields.add(new Node(i, j));
                }
            }
        }

        fieldVisited = new int[fields.size()];

        dfs(0,0);

        if(flag){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }

    static void dfs(int cnt, int startIndex) {
        if (flag || startIndex >= fieldVisited.length) {
            return;
        }

        if (cnt == 3) {
            flag = isAnswer();
            return;
        }

        for (int i = startIndex; i < fieldVisited.length; i++) {
            if(fieldVisited[i]==0){
                Node node = fields.get(i);
                data[node.x][node.y] = 'O';
                fieldVisited[i]=1;
                dfs(cnt+1, i+1);
                fieldVisited[i]=0;
                data[node.x][node.y] = 'X';
            }
        }

    }


    static boolean isAnswer() {
        for (Node node : teachers) {
            for (int i = 0; i < 4; i++) {
                int tx = node.x + dx[i];
                int ty = node.y + dy[i];

                while (true) {
                    if (tx < 0 || tx >= n || ty < 0 || ty >= n || data[tx][ty] == 'O') {
                        break;
                    }

                    if (data[tx][ty] == 'S') {
                        return false;
                    }

                    tx += dx[i];
                    ty += dy[i];
                }

            }

        }
        return true;
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

