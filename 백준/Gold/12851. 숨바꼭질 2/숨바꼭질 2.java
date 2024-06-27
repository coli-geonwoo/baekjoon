import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int[] visited = new int[200_001];
        for (int i = 0; i < visited.length; i++) {
            visited[i] = Integer.MAX_VALUE;

        }

        int start = Integer.parseInt(s[0]);
        int end = Integer.parseInt(s[1]);

        int cnt = 0;
        int result = Integer.MAX_VALUE;

        Deque<Data> q = new ArrayDeque<>();
        visited[start] = 0;
        q.add(new Data(start, 0));

        while (!q.isEmpty()) {
            Data data = q.pop();
            if (data.cnt > result) {
                continue;
            } else if (data.place == end && data.cnt < result) {
                result = data.cnt;
                visited[end] = data.cnt;
                cnt = 1;
                continue;
            } else if (data.place == end && data.cnt == result) {
                cnt++;
                continue;
            }

            int[] next = {data.place - 1, data.place + 1, data.place * 2};
            for (int next_place : next) {
                if(next_place >= visited.length || next_place <0 ||visited[next_place] < data.cnt+1){
                    continue;
                }
                visited[next_place] = data.cnt+1;
                q.add(new Data(next_place, data.cnt + 1));
            }
        }

        System.out.println(result);
        System.out.println(cnt);
    }

    static class Data {

        private int place;
        private int cnt;

        public Data(int place, int cnt) {
            this.place = place;
            this.cnt = cnt;
        }
    }
}
