
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int [][] visited;
    static int[] groupCnt;
    static int result;
    static List<Node> nodes = new ArrayList<>();
    static boolean [] checked;

    static int[][] data;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n][m];
        checked = new boolean[401];
        result =0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
                if (data[i][j] == 0) {
                    nodes.add(new Node(i, j));
                }
            }
        }

        dfs(0,0);

        System.out.println(result);

    }

    static void dfs(int startIndex, int cnt){
        if(cnt==2){

//            for (int i = 0; i < n; i++) {
//                for (int j = 0; j < m; j++) {
//                    System.out.print(data[i][j] + " ");
//                }
//                System.out.println();
//            }
//            System.out.println(countOneCase());
//            System.out.println();

            result= Math.max(countOneCase(), result);
            return;
        }

        for (int i = startIndex; i < nodes.size(); i++) {
            if(checked[i]==false){
                checked[i]=true;
                Node node = nodes.get(i);
                data[node.x][node.y]=1;
                dfs(i+1, cnt+1);
                checked[i]=false;
                data[node.x][node.y]=0;
            }
        }
    }



    static int countOneCase(){
        visited = new int [n][m];
        groupCnt = new int[401];
        int groupIndex = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(visited[i][j]==0 && data[i][j]==2){
                    countDeath(groupIndex++, i, j);
                }
            }
        }
        int sum=0;
        for (int i = 0; i < groupIndex; i++) {
            sum+= groupCnt[i];
        }

        return sum;
    }


    static void countDeath(int groupIndex, int x, int y){
        int cnt=1;
        Deque<Node> q = new ArrayDeque<>();
        q.add(new Node(x,y));
        visited[x][y]=1;

        boolean surroundFlag= true;

        while(!q.isEmpty()){
            Node currentNode = q.pollFirst();
            int cx = currentNode.x;
            int cy = currentNode.y;

            for (int i = 0; i < 4; i++) {
                int nx = cx+dx[i];
                int ny = cy+dy[i];

                if(nx<0 || nx>=n || ny<0 || ny>=m || visited[nx][ny]==1 || data[nx][ny]==1){
                    continue;
                }

                if(data[nx][ny]==0){
                    surroundFlag=false;
                    continue;
                }

                if(data[nx][ny]==2){
                    cnt+=1;
                    visited[nx][ny]=1;
                    q.add(new Node(nx, ny));

                }
            }
        }
        if(surroundFlag){
            groupCnt[groupIndex]= cnt;
        }
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

