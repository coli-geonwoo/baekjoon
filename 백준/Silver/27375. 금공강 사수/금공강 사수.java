
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

//16401
public class Main {
    // 금공강 사수
    static int[][] table = new int[5][10];
    static int result;
    static int n;
    static int k;
    static List<Node> nodes;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        nodes = new LinkedList<>();
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        k = Integer.parseInt(s[1]);
        result = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            nodes.add(new Node(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            ));
        }

        boolean[] checkList = new boolean[n];
        dfs(0, 0, checkList);

        System.out.println(result);
    }

    static class Node {
        int day;
        int start;
        int end;
        int score;

        public Node(int day, int start, int end) {
            this.day = day;
            this.start = start;
            this.end = end;
            this.score = end - start + 1;
        }

        public boolean checkTable(){
            for (int i = start-1; i <end ; i++) {
                if(table[day-1][i] == 1){
                    return false;
                }
            }
            return true;
        }

    }

    private static void dfs(int start, int score, boolean[] checkList) {
        if (score == k && checkFriday()) {
            result++;
            return;
        }

        for (int i = start; i < n; i++) {
            if (checkList[i]
                    || nodes.get(i).day == 5
                    || score + nodes.get(i).score > k
                    || !nodes.get(i).checkTable()) {
            } else {
                Node node = nodes.get(i);
                for (int j = node.start - 1; j <= node.end - 1; j++) {
                    table[node.day - 1][j] = 1;
                }

                checkList[i] = true;

                dfs(i+1, score + node.score, checkList);

                checkList[i] = false;
                for (int j = node.start - 1; j <= node.end - 1; j++) {
                    table[node.day - 1][j] = 0;
                }
            }
        }
    }

    private static boolean checkFriday() {
        for (int i = 0; i < 10; i++) {
            if (table[4][i] == 1) {
                return false;
            }
        }
        return true;
    }
}