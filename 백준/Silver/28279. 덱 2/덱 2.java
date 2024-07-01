
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static Deque<Integer> q = new ArrayDeque<Integer>();
    private static List<Integer> result = new ArrayList<Integer>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            if (s.length == 1) {
                func(Integer.parseInt(s[0]), Optional.empty());
                continue;
            }
            func(Integer.parseInt(s[0]), Optional.of(Integer.parseInt(s[1])));
        }

        for (int r : result) {
            System.out.println(r);
        }
    }

    private static void func(int op, Optional<Integer> x) {
        switch (op) {
            case 1:
                q.addFirst(x.get());
                break;
            case 2:
                q.addLast(x.get());
                break;
            case 3:
                if (q.isEmpty()) {
                    result.add(-1);
                    return;
                }
                result.add(q.pollFirst());
                break;
            case 4:
                if (q.isEmpty()) {
                    result.add(-1);
                    return;
                }
                result.add(q.pollLast());
                break;
            case 5:
                result.add(q.size());
                break;
            case 6:
                if (q.isEmpty()) {
                    result.add(1);
                    return;
                }
                result.add(0);
                break;
            case 7:
                if (q.isEmpty()) {
                    result.add(-1);
                    return;
                }
                result.add(q.peekFirst());
                break;
            case 8:
                if (q.isEmpty()) {
                    result.add(-1);
                    return;
                }
                result.add(q.peekLast());
                break;
        }

    }


}
