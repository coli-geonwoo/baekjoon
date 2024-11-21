
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringJoiner;

public class Main {
    //모음 : a e i o u
    // 0개 이상의 자음이 앞뒤로 붙어서 하나의 음이 된다.
    // h o  ng i k -> 3 C 2
    // h i c o n  -> 2 C 2
    static char[] mo = {'a', 'e', 'i', 'o', 'u'};
    static List<Integer> idxs;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringJoiner sj = new StringJoiner(System.lineSeparator());
        long mod = 1000000007;

        for (int k = 0; k < t; k++) {

            char[] str = br.readLine().toCharArray();
            idxs = new ArrayList<>();

            for (int i = 0; i < str.length; i++) {
                if (isMo(str[i])) {
                    idxs.add(i);
                }
            }

            if (idxs.isEmpty()) {
                sj.add("-1");
                continue;
            }

            long temp = 1;
            for (int i = 1; i < idxs.size(); i++) {
                temp = (temp * (idxs.get(i) - idxs.get(i - 1))) % mod;
            }



            sj.add(String.valueOf(temp));
        }
        System.out.println(sj);
    }

    static boolean isMo(char c) {
        for (int i = 0; i < mo.length; i++) {
            if (c == mo[i]) {
                return true;
            }
        }
        return false;
    }
}
