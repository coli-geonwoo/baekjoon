
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class Main {
    //2164. 카드2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        long n = Long.parseLong(br.readLine());

        Deque<Long> q = new ArrayDeque<>();

        for (long i = 1; i <= n; i++) {
            q.addLast(i);
        }

        while(q.size()!=1){
            q.pollFirst();
            q.addLast(q.pollFirst());
        }

        bw.write(q.pollFirst()+"\n");
        bw.flush();
    }
}

