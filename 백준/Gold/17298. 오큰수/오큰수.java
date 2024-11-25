import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        long n = Long.parseLong(br.readLine());
        long [] nums = new long[(int)n];
        Deque<Long> q = new ArrayDeque<>();
        Deque<Long> answers = new ArrayDeque<>();
        StringJoiner sj = new StringJoiner(" ");
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Long.parseLong(st.nextToken());
        }

        for (long i = n-1; i >= 0; i--) {
            long k = nums[(int)i];
            while(!q.isEmpty() && q.peekLast()<=k){
                q.pollLast();
            }

            if(q.isEmpty()){
                answers.add(-1L);
            }else{
                answers.add(q.peekLast());
            }
            q.add(k);
        }

        for (int i = 0; i < n; i++) {
            sj.add(String.valueOf(answers.pollLast()));
        }

        System.out.println(sj);
    }
}

