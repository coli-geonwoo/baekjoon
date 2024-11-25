
import static java.util.Comparator.comparing;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.StringJoiner;
import java.util.StringTokenizer;

public class Main {
    //2164. 카드2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Node> pq= new PriorityQueue<>(comparing(Node::getAbs).thenComparing(Node::getNum));

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            Node node = new Node(num);
            if(num!=0){
                pq.add(node);
            }else{
                if(pq.isEmpty()){
                    bw.write(0 + "\n");
                }else{
                    bw.write(pq.poll().num + "\n");
                }
            }
        }

        bw.flush();

    }

    static class Node{
        int abs;
        int num;

        public Node(int num) {
            this.abs = Math.abs(num);
            this.num = num;
        }

        public int getAbs() {
            return abs;
        }

        public int getNum() {
            return num;
        }
    }
}

