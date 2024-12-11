
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static int cnt1, cnt2, cnt3 = 0;
    static Map<Character, Character> next;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        //S- 가위 R - 바위 P - 보
        int n = Integer.parseInt(br.readLine());

        List<Character> dp1 = new ArrayList<>(); // 가위로 시작
        List<Character> dp2 = new ArrayList<>(); // 바위로 시작
        List<Character> dp3 = new ArrayList<>(); // 보로 시작

        dp1.add('P');
        dp2.add('R');
        dp3.add('S');

        next = new HashMap<>();
        next.put('R', 'S');
        next.put('S', 'P');
        next.put('P', 'R');

        char[] inputs = br.readLine().toCharArray();

        for (char input : inputs) {
            canNext(dp1, input, 1);
            canNext(dp2, input, 2);
            canNext(dp3, input, 3);
        }

        mod(dp1, 1);
        mod(dp2, 2);
        mod(dp3, 3);

        bw.write(String.valueOf(Math.min(cnt1, Math.min(cnt2, cnt3))));
        bw.flush();
        bw.close();
    }

    static void canNext(List<Character> dp, char input, int op) {
        if (!(next.get(dp.get(dp.size() - 1)) == input)) {
            if (op == 1) {
                cnt1++;
            }
            if (op == 2) {
                cnt2++;
            }
            if (op == 3) {
                cnt3++;
            }
        } else {
            dp.add(input);
        }
    }

    static void mod(List<Character> dp, int op) {
        while (dp.get(0) != dp.get(dp.size()-1)) {
            dp.remove(dp.size() - 1);
            if (op == 1) {
                cnt1++;
            }
            if (op == 2) {
                cnt2++;
            }
            if (op == 3) {
                cnt3++;
            }
        }
    }
}
