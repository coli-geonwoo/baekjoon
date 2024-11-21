
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringJoiner sj = new StringJoiner(" ");

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Deque<Node> nodes = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            Node node = new Node(i, nums[i]);

            if (nodes.isEmpty()) {
                nodes.add(node);
                sj.add(String.valueOf(nodes.peekFirst().num));
                continue;
            }

            while (!nodes.isEmpty() && nodes.peekLast().num > node.num) {
                nodes.removeLast();
            }

            while(!nodes.isEmpty() && (i- nodes.peekFirst().idx)>=m) {
                nodes.removeFirst();
            }
            nodes.add(node);
            sj.add(String.valueOf(nodes.peekFirst().num));
        }
        System.out.println(sj);
    }


    static class Node {
        int idx;
        int num;

        Node(int idx, int num) {
            this.idx = idx;
            this.num = num;
        }
    }
}

