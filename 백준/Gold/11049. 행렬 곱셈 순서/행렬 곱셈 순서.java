
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static int n;
    private static int dp[][];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        Node[] nodes = new Node[n];
        dp = new int[n][n];

        for(int i=0; i<n; i++){
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }

        int idx = 0;

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            int start = Integer.parseInt(s[0]);
            int end = Integer.parseInt(s[1]);
            nodes[idx++] = new Node(start, end, start * end);
            dp[i][i] = 0;
        }

        for (int df = 1; df <= n - 1; df++) {
            for (int st = 0; st <= n - 1 - df; st++) {
                for (int k = 0; k < df; k++) {
                    if(df==1){
                        Node s = nodes[st];
                        Node e = nodes[st+df];
                        dp[st][st+df] = s.start*s.end*e.end;
                        continue;
                    }

                    Node a = nodes[st];
                    Node b = nodes[st + k];
                    Node c = nodes[st + df];

                    dp[st][st + df] = Math.min(dp[st][st + df],
                            dp[st][st + k] + dp[st + k + 1][st + df] + a.start * b.end * c.end);
                }
            }
        }

        System.out.println(dp[0][n - 1]);
    }

    static class Node {
        int start;
        int end;
        int value;

        public Node(int start, int end, int value) {
            this.start = start;
            this.end = end;
            this.value = value;
        }

        int cal(Node node) {
            return start * node.start * node.end;
        }
    }


}
