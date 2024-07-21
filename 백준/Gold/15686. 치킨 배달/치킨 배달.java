
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

//29808 너의 수능 점수가 궁금해
public class Main {
    static int chickenDistance;
    static boolean [] visited;
    static int k;
    static List<Node> houses = new ArrayList<>();
    static List<Node> chickenZips = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        k = Integer.parseInt(s[1]);
        int [][] data = new int[n][n];

        chickenDistance = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());

                if(data[i][j] ==1){
                    houses.add(new Node(i, j));
                }

                if(data[i][j]==2){
                    chickenZips.add(new Node(i, j));
                }
            }
        }

        visited = new boolean[chickenZips.size()];


        dfs(0,0,new ArrayList<>());

        System.out.println(chickenDistance);
    }

    static void dfs(int startIndex, int count, List<Node> chickens){
        if(count==k){
            int temp = 0;
            for(Node house: houses){
                temp += house.chickenDistance(chickens);
            }
            chickenDistance = Math.min(chickenDistance,temp);
            return;
        }

        for (int i = startIndex; i < chickenZips.size(); i++) {
            if(visited[i]){
                continue;
            }
            visited[i]=true;
            chickens.add(chickenZips.get(i));
            dfs(i+1, count+1, chickens);
            chickens.remove(chickens.size()-1);
            visited[i]=false;
        }

    }

    static class Node {
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        int chickenDistance(List<Node> zips){
            int result= Integer.MAX_VALUE;

            for (Node zip : zips){
                int distance = Math.abs(zip.x - x) + Math.abs(zip.y-y);
                result = Math.min(result,distance);
            }
            return result;
        }
                
    }

}