
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 층수
        int m = Integer.parseInt(st.nextToken()); // 참여자의 수
        int[] hands = new int[2 * m];

        List<Hand> handList = new ArrayList<Hand>();

        for (int i = 1; i < m + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int firstHand = Integer.parseInt(st.nextToken());
            int secondHand = Integer.parseInt(st.nextToken());
            handList.add(new Hand(firstHand-1, i));
            handList.add(new Hand(secondHand-1, i));
        }

        Collections.sort(handList);

        for (int i = 0; i < handList.size(); i++) {
            hands[i] = handList.get(i).num;
        }
//
//        for (int i = 0; i < 2*m; i++) {
//            System.out.print(hands[i] + " ");
//        }
//
//        System.out.println();
        System.out.println(hands[(n - 1) % (2 * m)]);
    }

    static class Hand implements Comparable<Hand>{
        int height;
        int num;

        public Hand(int height, int num) {
            this.height = height;
            this.num = num;
        }

        @Override
        public int compareTo(Hand o) {
            return Integer.compare(height, o.height);
        }
    }
}
