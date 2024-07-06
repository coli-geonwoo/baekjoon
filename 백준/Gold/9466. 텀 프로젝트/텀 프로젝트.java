
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    static int[] student;
    static int sum;
    static boolean[] team;
    static boolean[] visited;


    //9466. 텀 프로젝트
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            System.out.println(turn(br));
        }
    }

    private static int turn(BufferedReader br) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        team = new boolean[n];
        visited = new boolean[n];
        student = new int[n];
        int idx = 0;

        while (st.hasMoreTokens()) {
            student[idx++] = Integer.parseInt(st.nextToken()) - 1;
        }
        sum=0;
        for (int i = 0; i < n; i++) {
            dfs(i);
        }

        return n - sum;
    }

    private static void dfs(int idx) {

        //이미 팀이 있다면
        if(team[idx]){
            return;
        }
        //방문한적이 있다면 -> 다시 돌아온 케이스
        if(visited[idx]){
            team[idx]=true;
            sum++;
        }

        visited[idx]=true;
        dfs(student[idx]);
        team[idx]=true;
        visited[idx]=false;
    }
}
