import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[][] board;
    static int n;
    static int result;

    //12100. 2048
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        //보드 초기화
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j]= Integer.parseInt(st.nextToken());
            }
        }

        dfs(0);

        System.out.println(result);
    }

    private static void dfs(int depth){
        if (depth==5){
//            printboard();
//            System.out.println();

            initResult(); //최대값 갱신
            return;
        }

        int [][] temp = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp[i][j]= board[i][j];
            }
        }


        for(int i=0; i<4; i++){
            board = play(i);
            dfs(depth+1);
            board = temp;
        }
    }

    private static void printboard() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static void initResult(){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                result = Math.max(board[i][j], result);
            }
        }
    }

    private static int[][] play(int op){
        if(op==0){
            return left();
        }

        if(op==1){
            return right();
        }

        if(op==2){
            return up();
        }

        if(op==3){
            return down();
        }

        return null;
    }


    private static int[][] left() {
        int[][] temp = new int[n][n];

        for (int i = 0; i < n; i++) {
            int idx = 0;
            int before = -1;
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) {
                    continue;
                }

                if (before != board[i][j]) {
                    if (before != -1) {
                        temp[i][idx++] = before;
                    }
                    before = board[i][j];
                    continue;
                }

                if (board[i][j] == before) {
                    temp[i][idx++] = before * 2;
                    before = -1;
                }
            }

            if (idx != n) {
                while (idx != n) {
                    if (before != -1) {
                        temp[i][idx++] = before;
                        before=-1;
                        continue;
                    }
                    temp[i][idx++] = 0;
                }
            }
        }
        return temp;
    }

    private static int[][] right() {
        int[][] temp = new int[n][n];

        for (int i = 0; i < n; i++) {
            int idx = n-1;
            int before = -1;
            for (int j = n-1; j >= 0; j--) {
                if (board[i][j] == 0) {
                    continue;
                }

                if (before != board[i][j]) {
                    if (before != -1) {
                        temp[i][idx--] = before;
                    }
                    before = board[i][j];
                    continue;
                }

                if (board[i][j] == before) {
                    temp[i][idx--] = before * 2;
                    before = -1;
                }
            }

            if (idx != -1) {
                while (idx != -1) {
                    if (before != -1) {
                        temp[i][idx--] = before;
                        before = -1;
                        continue;
                    }
                    temp[i][idx--] = 0;
                }
            }
        }
        return temp;
    }

    private static int[][] up() {
        int[][] temp = new int[n][n];


        for (int i = 0; i < n; i++) {
            int idx = 0;
            int before = -1;
            for (int j = 0; j < n; j++) {
                if (board[j][i] == 0) {
                    continue;
                }

                if (before != board[j][i]) {
                    if (before != -1) {
                        temp[idx++][i] = before;
                    }
                    before = board[j][i];
                    continue;
                }

                if (board[j][i] == before) {
                    temp[idx++][i] = before * 2;
                    before = -1;
                }
            }

            if (idx != n) {
                while (idx != n) {
                    if (before != -1) {
                        temp[idx++][i] = before;
                        before = -1;
                        continue;
                    }
                    temp[idx++][i] = 0;
                }
            }
        }
        return temp;
    }

    private static int[][] down() {
        int[][] temp = new int[n][n];


        for (int i = 0; i < n; i++) {
            int idx = n-1;
            int before = -1;
            for (int j = n-1; j >= 0; j--) {
                if (board[j][i] == 0) {
                    continue;
                }

                if (before != board[j][i]) {
                    if (before != -1) {
                        temp[idx--][i] = before;
                    }
                    before = board[j][i];

                    continue;
                }

                if (board[j][i] == before) {
                    temp[idx--][i] = before * 2;
                    before = -1;
                }
            }

            if (idx != -1) {
                while (idx != -1) {
                    if (before != -1) {
                        temp[idx--][i] = before;
                        before  = -1;
                        continue;
                    }
                    temp[idx--][i] = 0;
                }
            }
        }
        return temp;
    }

}
