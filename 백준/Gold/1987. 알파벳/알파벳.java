
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    static int [] dx = {-1,1,0,0};
    static int [] dy= {0,0,-1,1};
    static String [][] data;
    static int row;
    static int col;
    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        row = Integer.parseInt(s[0]);
        col = Integer.parseInt(s[1]);
        data = new String[row][col];
        result=0;

        for (int i = 0; i < row; i++) {
            data[i] = br.readLine().split("");
        }
        Map<String, Boolean> path = new HashMap<>();
        path.put(data[0][0], true);

        dfs(1, 0,0, path);
        System.out.println(result);

    }

    private static void dfs(int cnt, int x, int y, Map<String, Boolean> path){
        boolean flag = false;

        for (int i = 0; i < 4; i++) {
            int nx = x+dx[i];
            int ny = y+dy[i];

            if(nx<0 || ny<0 || nx>=row || ny>=col || path.getOrDefault(data[nx][ny], false)){
                continue;
            }
            flag=true;
            path.put(data[nx][ny], true);
            dfs(cnt+1, nx, ny, path);
            path.remove(data[nx][ny]);
        }

        if(flag==false){
            result = Math.max(result,cnt);
        }
    }

}
